#!/usr/bin/env python3
"""
Shared Reddit client for all metric collectors.

Uses the public Reddit JSON endpoint (www.reddit.com/.json).
This works from residential/local IPs but is blocked from datacenter IPs
(GitHub Actions). Reddit collection must be run locally.

Run locally:  python run_weekly_update.py --reddit-only
"""

import time
import requests

_USER_AGENT = "AbsurdityIndex/1.0 (research project; github.com/Surfrrosa/absurdity-index)"


def search_subreddit(subreddit, query, limit=25):
    """Search a subreddit via public JSON endpoint. Returns list of post dicts."""
    url = f"https://www.reddit.com/r/{subreddit}/search.json"
    params = {
        "q": query,
        "restrict_sr": 1,
        "sort": "top",
        "t": "month",
        "limit": limit,
    }
    headers = {"User-Agent": _USER_AGENT}

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
        elif response.status_code == 403:
            print(f"    Blocked (403) on r/{subreddit}. Reddit blocks datacenter IPs.")
            print("    Run Reddit collectors locally: python run_weekly_update.py --reddit-only")
            return []
        else:
            print(f"    Error {response.status_code} searching r/{subreddit}")
            return []
    except Exception as e:
        print(f"    Exception searching r/{subreddit}: {e}")
        return []


def is_authenticated():
    """Always True for public JSON endpoint (no auth needed)."""
    return True
