#!/usr/bin/env python3
"""
Shared Reddit OAuth2 client for all metric collectors.

Uses OAuth2 client_credentials grant (application-only, read-only access).
This authenticates via oauth.reddit.com, which works from datacenter IPs
(GitHub Actions). The old www.reddit.com/search.json endpoint is blocked
from cloud IPs with 403.

Required env vars: REDDIT_CLIENT_ID, REDDIT_CLIENT_SECRET
Create a "script" or "installed" app at: https://www.reddit.com/prefs/apps

Also add these as GitHub repo secrets for CI.
"""

import os
import sys
import time
import requests
from pathlib import Path
from dotenv import load_dotenv

# Load .env from the data-collection directory
SCRIPT_DIR = Path(__file__).resolve().parent
load_dotenv(SCRIPT_DIR / ".env")

_TOKEN = None
_TOKEN_EXPIRES = 0
_USER_AGENT = "AbsurdityIndex/1.0 (research project; github.com/Surfrrosa/absurdity-index)"


def _get_token():
    """Get or refresh an OAuth2 application-only token."""
    global _TOKEN, _TOKEN_EXPIRES

    now = time.time()
    if _TOKEN and now < _TOKEN_EXPIRES - 60:
        return _TOKEN

    client_id = os.environ.get("REDDIT_CLIENT_ID", "")
    client_secret = os.environ.get("REDDIT_CLIENT_SECRET", "")

    if not client_id or not client_secret:
        print("WARNING: REDDIT_CLIENT_ID and REDDIT_CLIENT_SECRET not set.")
        print("  Reddit collection requires OAuth2 credentials.")
        print("  Create an app at https://www.reddit.com/prefs/apps")
        return None

    try:
        resp = requests.post(
            "https://www.reddit.com/api/v1/access_token",
            auth=requests.auth.HTTPBasicAuth(client_id, client_secret),
            data={"grant_type": "client_credentials"},
            headers={"User-Agent": _USER_AGENT},
            timeout=15,
        )
        if resp.status_code == 200:
            data = resp.json()
            _TOKEN = data["access_token"]
            _TOKEN_EXPIRES = now + data.get("expires_in", 3600)
            return _TOKEN
        else:
            print(f"  OAuth token request failed: HTTP {resp.status_code}")
            return None
    except Exception as e:
        print(f"  OAuth exception: {e}")
        return None


def search_subreddit(subreddit, query, limit=25):
    """Search a subreddit via OAuth2 endpoint. Returns list of post dicts."""
    token = _get_token()
    if not token:
        return []

    url = f"https://oauth.reddit.com/r/{subreddit}/search"
    params = {
        "q": query,
        "restrict_sr": 1,
        "sort": "top",
        "t": "month",
        "limit": limit,
    }
    headers = {
        "Authorization": f"Bearer {token}",
        "User-Agent": _USER_AGENT,
    }

    try:
        response = requests.get(url, headers=headers, params=params, timeout=15)
        if response.status_code == 200:
            data = response.json()
            if "data" in data and "children" in data["data"]:
                return data["data"]["children"]
            return []
        elif response.status_code == 429:
            print(f"    Rate limited on r/{subreddit}, waiting 10s...")
            time.sleep(10)
            response = requests.get(url, headers=headers, params=params, timeout=15)
            if response.status_code == 200:
                data = response.json()
                if "data" in data and "children" in data["data"]:
                    return data["data"]["children"]
            print(f"    Still rate limited: r/{subreddit}")
            return []
        elif response.status_code == 401:
            # Token expired mid-run, force refresh
            global _TOKEN
            _TOKEN = None
            token = _get_token()
            if token:
                headers["Authorization"] = f"Bearer {token}"
                response = requests.get(url, headers=headers, params=params, timeout=15)
                if response.status_code == 200:
                    data = response.json()
                    if "data" in data and "children" in data["data"]:
                        return data["data"]["children"]
            return []
        else:
            print(f"    Error {response.status_code} searching r/{subreddit}")
            return []
    except Exception as e:
        print(f"    Exception searching r/{subreddit}: {e}")
        return []


def is_authenticated():
    """Check if we can get a valid token. Call early to fail fast."""
    return _get_token() is not None
