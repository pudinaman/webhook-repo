# GitHub Activity Feed 🚀

A real-time dashboard that captures GitHub events (Push, Pull Request, Merge) and displays them on a sleek, modern React interface.

## 🏗️ Architecture

- **Frontend**: React 19 + Vite + Tailwind CSS v4 (Glassmorphism design).
- **Backend**: Flask Application Factory pattern.
- **Database**: MongoDB Atlas (Cloud storage).
- **Tunneling**: ngrok (To receive local webhooks from GitHub).

---

## 🛠️ Setup Instructions

### 1. Prerequisites
- Python 3.9+
- Node.js & npm
- [ngrok](https://ngrok.com/) account
- MongoDB Atlas account (for connection string)

### 2. Backend Setup (`/webhook-repo`)
1. **Navigate to the directory**:
   ```bash
   cd webhook-repo
   ```
2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
3. **Configure Environment**:
   Create a `.env` file inside `webhook-repo/` (you can copy the provided `.env.example`):
   ```bash
   cp .env.example .env
   ```
   *Note: `.env.example` already contains your MongoDB Atlas link.*
4. **Run the server**:
   ```bash
   python run.py
   ```

### 3. Frontend Setup (`/webhook-repo/frontend`)
1. **Navigate to the directory**:
   ```bash
   cd webhook-repo/frontend
   ```
2. **Install dependencies**:
   ```bash
   npm install
   ```
3. **Run the React Dev Server**:
   ```bash
   npm run dev
   ```

### 4. GitHub Webhook Integration (Via ngrok)
1. **Start ngrok**:
   ```bash
   ngrok http 5000
   ```
2. **Configure Webhook**:
   - Go to your GitHub Repository -> **Settings** -> **Webhooks** -> **Add Webhook**.
   - **Payload URL**: `YOUR_NGROK_URL/webhook` (e.g., `https://xxxx.ngrok-free.dev/webhook`).
   - **Content type**: `application/json`.
   - **Which events?**: Select **Pushes** and **Pull Requests**.
3. **Test**: Push a commit to your repo and watch it appear in the dashboard!

---

## 📂 Project Structure

```text
├── webhook-repo/           # Main Project Folder
│   ├── app/                # Flask Application Package
│   │   ├── models.py       # MongoDB Logic
│   │   ├── routes.py       # API & Webhook Endpoints
│   │   └── __init__.py     # App Factory
│   ├── frontend/           # React Application (Vite)
│   │   ├── src/            # Components & Logic
│   │   └── tailwind.config.js
│   ├── run.py              # Backend Entry Point
│   ├── config.py           # Config Management
│   └── requirements.txt    # Python Dependencies
├── simulate_webhook.py      # Script to test webhooks locally
└── README.md               # You are here!
```

## 🎥 Testing locally
If you don't want to push to GitHub, run the simulation script:
```bash
python simulate_webhook.py
```
*(Make sure to update the URL in local `.env` if needed)*.
