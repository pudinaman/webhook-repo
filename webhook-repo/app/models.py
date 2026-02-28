from pymongo import MongoClient
from flask import current_app

_client = None

def get_db():
    global _client
    if _client is None:
        _client = MongoClient(current_app.config['MONGO_URI'])
    return _client['github_webhooks']

def insert_action(action_data):
    """Inserts a new action into MongoDB."""
    db = get_db()
    return db['actions'].insert_one(action_data)

def get_latest_actions(limit=10):
    """Retrieves the latest actions from MongoDB."""
    db = get_db()
    return list(db['actions'].find().sort("timestamp", -1).limit(limit))
