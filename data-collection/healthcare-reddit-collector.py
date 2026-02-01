#!/usr/bin/env python3
"""
Reddit JSON Collector - Healthcare (What Healthcare?)
Uses public Reddit JSON endpoints - NO API KEY NEEDED

Collects posts from healthcare-related subreddits using search terms
and categorizes by severity (Level 1/2/3)
"""

import requests
import time
import csv
import json
from datetime import datetime

# Subreddits to collect from
SUBREDDITS = [
    'HealthInsurance',
    'Insurance',
    'povertyfinance',
    'ChronicIllness',
    'diabetes',
    'cancer'
]

# Search terms for healthcare struggles
SEARCH_TERMS = [
    'claim denied',
    'can\'t afford treatment',
    'prior authorization',
    'medical debt',
    'insurance won\'t cover',
    'appeal denied',
    'out of network',
    'surprise bill'
]

# Level 3 (Crisis) keywords
LEVEL_3_KEYWORDS = [
    'bankruptcy', 'collections', 'medical debt', 'going broke',
    'can\'t afford treatment', 'life-saving', 'cancer treatment',
    'dying', 'emergency', 'life or death', 'denied life-saving',
    'denied cancer treatment', 'filed for bankruptcy'
]

# Level 2 (Struggling) keywords
LEVEL_2_KEYWORDS = [
    'denied', 'claim denied', 'rejected', 'appeal denied',
    'won\'t cover', 'can\'t afford', 'prior authorization',
    'can\'t afford insulin', 'high deductible', 'out of pocket',
    'surprise bill', 'out of network'
]

def get_reddit_json(url, params=None):
    """Fetch JSON from Reddit public endpoint with retry logic"""
    headers = {
        'User-Agent': 'Mozilla/5.0 (compatible; AbsurdityIndexResearch/1.0; Academic Research Project)'
    }

    for attempt in range(3):
        try:
            response = requests.get(url, headers=headers, params=params, timeout=15)
            if response.status_code == 200:
                return response.json()
            elif response.status_code in (403, 429):
                wait = 10 * (attempt + 1)
                print(f"  ⏳ {response.status_code} on attempt {attempt + 1}, retrying in {wait}s...")
                time.sleep(wait)
                continue
            else:
                print(f"  ✗ Error {response.status_code}: {url}")
                return None
        except Exception as e:
            print(f"  ✗ Exception fetching {url}: {e}")
            return None

    print(f"  ✗ Failed after 3 attempts: {url}")
    return None

def search_subreddit(subreddit, query, limit=25):
    """Search a subreddit via JSON endpoint"""
    url = f'https://www.reddit.com/r/{subreddit}/search.json'
    params = {
        'q': query,
        'restrict_sr': 1,  # Restrict to this subreddit
        'sort': 'top',
        't': 'month',  # Last month
        'limit': limit
    }

    data = get_reddit_json(url, params)

    if data and 'data' in data and 'children' in data['data']:
        return data['data']['children']
    return []

def categorize_post(title, selftext):
    """Categorize post into Level 1/2/3"""
    text = (title + " " + selftext).lower()

    # Count Level 3 keywords
    level_3_count = sum(1 for keyword in LEVEL_3_KEYWORDS if keyword in text)

    # Count Level 2 keywords
    level_2_count = sum(1 for keyword in LEVEL_2_KEYWORDS if keyword in text)

    # Level 3: 2+ crisis keywords OR critical phrases
    if level_3_count >= 2 or any(phrase in text for phrase in [
        'filed for bankruptcy', 'going to die', 'denied life-saving',
        'can\'t afford cancer', 'medical bankruptcy'
    ]):
        return 'LEVEL_3_CRISIS'

    # Level 2: 2+ struggling keywords OR common frustration phrases
    elif level_2_count >= 2 or any(phrase in text for phrase in [
        'claim denied', 'appeal denied', 'prior authorization',
        'can\'t afford', 'won\'t cover'
    ]):
        return 'LEVEL_2_STRUGGLING'

    # Level 1: Default
    else:
        return 'LEVEL_1_AWARE'

def collect_from_subreddit(subreddit, search_terms, posts_per_term=15):
    """Collect posts from a subreddit"""
    print(f"\n📍 Collecting from r/{subreddit}")

    all_posts = []
    seen_ids = set()

    for term in search_terms:
        print(f"  Searching: '{term}'")

        posts = search_subreddit(subreddit, term, limit=posts_per_term)

        for post_data in posts:
            post = post_data['data']
            post_id = post['id']

            # Skip duplicates
            if post_id in seen_ids:
                continue
            seen_ids.add(post_id)

            # Extract data
            title = post.get('title', '')
            selftext = post.get('selftext', '')
            url = f"https://www.reddit.com{post.get('permalink', '')}"
            score = post.get('score', 0)
            num_comments = post.get('num_comments', 0)
            created_utc = post.get('created_utc', 0)
            author = post.get('author', '[deleted]')

            # Convert timestamp to date
            date = datetime.fromtimestamp(created_utc).strftime('%Y-%m-%d')

            # Categorize
            category = categorize_post(title, selftext)

            all_posts.append({
                'subreddit': subreddit,
                'post_id': post_id,
                'title': title,
                'selftext_snippet': selftext[:300] if selftext else '',  # First 300 chars
                'url': url,
                'score': score,
                'num_comments': num_comments,
                'author': author,
                'created_date': date,
                'search_term': term,
                'category': category
            })

            # Show progress
            icon = '🔴' if 'CRISIS' in category else '🟡' if 'STRUGGLING' in category else '🟢'
            print(f"    {icon} {title[:60]}...")

        # Be respectful with rate limiting
        time.sleep(2)

    print(f"  ✓ Collected {len(all_posts)} unique posts from r/{subreddit}")
    return all_posts

def main():
    """Main collection process"""
    print("=" * 80)
    print("REDDIT HEALTHCARE DATA COLLECTION (JSON Endpoints)")
    print("=" * 80)
    print("\nUsing public JSON endpoints - no API key needed!")
    print(f"\nCollecting from {len(SUBREDDITS)} subreddits:")
    for sub in SUBREDDITS:
        print(f"  - r/{sub}")
    print(f"\nUsing {len(SEARCH_TERMS)} search terms")

    all_posts = []

    # Collect from each subreddit
    for subreddit in SUBREDDITS:
        posts = collect_from_subreddit(subreddit, SEARCH_TERMS, posts_per_term=10)
        all_posts.extend(posts)

        # Rate limiting between subreddits
        time.sleep(3)

    # Remove duplicates (same post might appear in multiple searches)
    unique_posts = {}
    for post in all_posts:
        unique_posts[post['post_id']] = post

    all_posts = list(unique_posts.values())

    # Calculate statistics
    total = len(all_posts)
    level_3 = len([p for p in all_posts if p['category'] == 'LEVEL_3_CRISIS'])
    level_2 = len([p for p in all_posts if p['category'] == 'LEVEL_2_STRUGGLING'])
    level_1 = len([p for p in all_posts if p['category'] == 'LEVEL_1_AWARE'])

    print("\n" + "=" * 80)
    print("COLLECTION COMPLETE")
    print("=" * 80)
    print(f"\nTotal unique posts: {total}")
    print(f"\nBreakdown:")
    if total > 0:
        print(f"  Level 3 (Crisis):      {level_3} ({level_3/total*100:.1f}%)")
        print(f"  Level 2 (Struggling):  {level_2} ({level_2/total*100:.1f}%)")
        print(f"  Level 1 (Aware):       {level_1} ({level_1/total*100:.1f}%)")
    else:
        print("  No posts collected - Reddit may be blocking requests")

    crisis_ratio = (level_2 + level_3) / total * 100 if total > 0 else 0
    print(f"\n  Crisis ratio (L2+L3):  {crisis_ratio:.1f}%")

    # Save to CSV
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    filename = f'collected-data/healthcare_reddit_{timestamp}.csv'

    with open(filename, 'w', newline='', encoding='utf-8') as f:
        fieldnames = ['subreddit', 'post_id', 'title', 'selftext_snippet',
                     'url', 'score', 'num_comments', 'author', 'created_date',
                     'search_term', 'category']
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(all_posts)

    print(f"\n✓ Data saved to: {filename}")
    print("=" * 80)

if __name__ == '__main__':
    main()
