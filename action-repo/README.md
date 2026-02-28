# action-repo

This repository is used to trigger GitHub Webhooks. 

### Webhook Configuration
To set up the webhook:
1. Go to **Settings > Webhooks > Add webhook**.
2. **Payload URL**: Enter your `webhook-repo` URL (e.g., using `ngrok` for local development).
3. **Content type**: `application/json`.
4. **Events**: Select `Push`, `Pull Request`.
5. **Secret**: (Optional) as per your setup.

### Simulated Events
Use the `simulate_webhook.py` script in the root to test the functionality without needing real GitHub actions.
