# Reddit API Setup Instructions

## Quick Setup (5 minutes)

### 1. Create Reddit App

1. Go to: https://www.reddit.com/prefs/apps
2. Scroll to bottom, click "create another app..." or "are you a developer? create an app..."
3. Fill in:
   - **Name:** Disappointments Dashboard
   - **App type:** Select "script"
   - **Description:** Data collection for disappointments dashboard research
   - **About URL:** (leave blank)
   - **Redirect URI:** http://localhost:8080
4. Click "create app"

### 2. Get Your Credentials

You'll see:
- **client_id:** String under "personal use script" (looks like: dQw4w9WgXcQ)
- **client_secret:** String next to "secret" (looks like: 1234567890abcdefghij)

### 3. Create .env File

In `/Volumes/Extreme SSD/Home/projects/disappointments-dashboard/data/`, create a file named `.env`:

```
REDDIT_CLIENT_ID=your_client_id_here
REDDIT_CLIENT_SECRET=your_client_secret_here
REDDIT_USER_AGENT=DisappointmentsDashboard/1.0 by /u/your_username
```

Replace:
- `your_client_id_here` with your actual client ID
- `your_client_secret_here` with your actual secret
- `your_username` with your Reddit username

### 4. Install python-dotenv

```bash
pip3 install python-dotenv
```

### 5. Run the Script

```bash
cd "/Volumes/Extreme SSD/Home/projects/disappointments-dashboard/data"
python3 collect_reddit_ai_psychosis.py
```

## What It Does

- Collects 100 posts from r/CharacterAI
- Collects 100 posts from r/replika
- Searches for crisis keywords in titles and text
- Outputs CSV with posts flagged for manual review
- You categorize each as Level 1/2/3
- Calculate crisis ratio

## Rate Limits

- Reddit API: 60 requests/minute
- Our script: ~10 requests total (well within limits)
- Safe to run multiple times

## Troubleshooting

**Error: "received 401 HTTP response"**
- Your credentials are wrong
- Check .env file
- Make sure no extra spaces

**Error: "module 'praw' not found"**
- Run: `pip3 install praw`

**Error: "module 'dotenv' not found"**
- Run: `pip3 install python-dotenv`

## Privacy & Ethics

- Only collects publicly visible posts
- No private messages
- No user tracking
- Anonymize all data in dashboard
- Respect Reddit's ToS
