# YouTube Data API v3 Setup

## Step 1: Get API Key

1. Go to Google Cloud Console: https://console.cloud.google.com/
2. Create a new project (or select existing)
   - Click "Select a project" dropdown at top
   - Click "NEW PROJECT"
   - Name: "Disappointments Dashboard"
   - Click "CREATE"

3. Enable YouTube Data API v3
   - Go to "APIs & Services" > "Library"
   - Search for "YouTube Data API v3"
   - Click it and press "ENABLE"

4. Create API Credentials
   - Go to "APIs & Services" > "Credentials"
   - Click "+ CREATE CREDENTIALS" at top
   - Select "API key"
   - Copy the API key that appears
   - (Optional) Click "RESTRICT KEY" and limit to YouTube Data API v3 only

## Step 2: Add to .env File

Add this line to your `.env` file:

```
YOUTUBE_API_KEY=your_api_key_here
```

## Step 3: Install YouTube API Client

```bash
pip install google-api-python-client
```

## API Limits

- Free quota: 10,000 units per day
- Search query: 100 units
- Video details: 1 unit
- We can do ~100 searches per day or ~160 video samplings

## Search Terms for AI Psychosis

1. "my AI girlfriend"
2. "addicted to Character.AI"
3. "Replika breakup"
4. "in love with AI"
5. "AI boyfriend"
6. "Character AI addiction"
7. "Replika emotional attachment"
8. "AI companion mental health"

Each search will get top 20 results = 160 total videos
