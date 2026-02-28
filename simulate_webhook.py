import requests
import json
import time
from datetime import datetime
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Use environment variable or fallback to localhost
WEBHOOK_URL = os.getenv("WEBHOOK_URL", "http://localhost:5000/webhook")

def send_push():
    payload = {
        "pusher": {"name": "Travis"},
        "ref": "refs/heads/staging"
    }
    headers = {"X-GitHub-Event": "push", "Content-Type": "application/json"}
    response = requests.post(WEBHOOK_URL, data=json.dumps(payload), headers=headers)
    print(f"Push response: {response.status_code}")

def send_pr():
    payload = {
        "action": "opened",
        "pull_request": {
            "user": {"login": "Travis"},
            "head": {"ref": "staging"},
            "base": {"ref": "master"},
            "updated_at": "2021-04-01T09:00:00Z"
        }
    }
    headers = {"X-GitHub-Event": "pull_request", "Content-Type": "application/json"}
    response = requests.post(WEBHOOK_URL, data=json.dumps(payload), headers=headers)
    print(f"PR response: {response.status_code}")

def send_merge():
    payload = {
        "action": "closed",
        "pull_request": {
            "user": {"login": "Travis"},
            "head": {"ref": "dev"},
            "base": {"ref": "master"},
            "merged": True,
            "updated_at": "2021-04-02T12:00:00Z"
        }
    }
    headers = {"X-GitHub-Event": "pull_request", "Content-Type": "application/json"}
    response = requests.post(WEBHOOK_URL, data=json.dumps(payload), headers=headers)
    print(f"Merge response: {response.status_code}")

if __name__ == "__main__":
    print("Simulating GitHub events...")
    send_push()
    time.sleep(1)
    send_pr()
    time.sleep(1)
    send_merge()
