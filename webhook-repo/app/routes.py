from flask import Blueprint, request, jsonify, render_template
from app.models import insert_action, get_latest_actions
from datetime import datetime
import pytz

bp = Blueprint('main', __name__)

def format_timestamp(ts_str):
    """Formats GitHub timestamp to '1st April 2021 - 9:30 PM UTC'"""
    try:
        dt = datetime.strptime(ts_str, "%Y-%m-%dT%H:%M:%SZ")
        dt = dt.replace(tzinfo=pytz.UTC)
        
        day = dt.day
        if 4 <= day <= 20 or 24 <= day <= 30:
            suffix = "th"
        else:
            suffix = ["st", "nd", "rd"][day % 10 - 1]
            
        return dt.strftime(f"{day}{suffix} %B %Y - %I:%M %p %Z")
    except Exception:
        return ts_str

@bp.route('/')
def index():
    return render_template('index.html')

@bp.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    if not data:
        return jsonify({"error": "No data received"}), 400

    event_type = request.headers.get('X-GitHub-Event')
    action_data = {
        "author": "Unknown",
        "from_branch": "",
        "to_branch": "",
        "timestamp": datetime.now(pytz.UTC).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "request_type": ""
    }

    if event_type == 'push':
        action_data["author"] = data.get("pusher", {}).get("name", "Unknown")
        action_data["to_branch"] = data.get("ref", "").split("/")[-1]
        action_data["request_type"] = "PUSH"
        
    elif event_type == 'pull_request':
        pr = data.get("pull_request", {})
        action_data["author"] = pr.get("user", {}).get("login", "Unknown")
        action_data["from_branch"] = pr.get("head", {}).get("ref", "")
        action_data["to_branch"] = pr.get("base", {}).get("ref", "")
        
        if data.get("action") == "closed" and pr.get("merged"):
            action_data["request_type"] = "MERGE"
        else:
            action_data["request_type"] = "PULL_REQUEST"
            
        action_data["timestamp"] = pr.get("updated_at", action_data["timestamp"])

    if action_data["request_type"]:
        insert_action(action_data)
        return jsonify({"status": "success"}), 200
    
    return jsonify({"status": "ignored"}), 200

@bp.route('/api/actions', methods=['GET'])
def get_actions():
    actions = get_latest_actions()
    formatted_actions = []
    for action in actions:
        action['_id'] = str(action['_id'])
        ts = format_timestamp(action['timestamp'])
        if action['request_type'] == "PUSH":
            action['message'] = f'"{action["author"]}" pushed to "{action["to_branch"]}" on {ts}'
        elif action['request_type'] == "PULL_REQUEST":
            action['message'] = f'"{action["author"]}" submitted a pull request from "{action["from_branch"]}" to "{action["to_branch"]}" on {ts}'
        elif action['request_type'] == "MERGE":
            action['message'] = f'"{action["author"]}" merged branch "{action["from_branch"]}" to "{action["to_branch"]}" on {ts}'
        formatted_actions.append(action)
        
    return jsonify(formatted_actions)
