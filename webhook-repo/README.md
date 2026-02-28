# webhook-repo

This repository contains the Flask backend and the Activity Feed UI for capturing GitHub webhooks and storing them in MongoDB Atlas.

### Tech Stack
- **Backend**: Flask (Python)
- **Database**: MongoDB Atlas
- **Frontend**: Tailwind CSS, Vanilla JS

### Project Structure
- `run.py`: Entry point for the application.
- `config.py`: Configuration management.
- `app/`:
    - `__init__.py`: Application factory.
    - `routes.py`: API and view routes.
    - `models.py`: Database logic.
    - `templates/`: UI components.
- `simulate_webhook.py`: (Root) Testing tool.

### Setup
1. **Pip Install**:
   ```bash
   pip install -r requirements.txt
   ```
2. **Configure**: Update `.env` with your `MONGO_URI`.
3. **Launch Server**:
   Make sure you are in the `webhook-repo` directory:
   ```bash
   python run.py
   ```
3. **Open Browser**: Go to `http://127.0.0.1:5000` to see the Activity Feed.
