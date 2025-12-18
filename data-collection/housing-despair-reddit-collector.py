#!/usr/bin/env python3
"""
Collect Reddit posts about housing despair and homeownership crisis
Uses PRAW (Python Reddit API Wrapper) to systematically sample posts
"""

import os
import praw
import pandas as pd
from datetime import datetime
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Reddit API setup
REDDIT_CLIENT_ID = os.getenv('REDDIT_CLIENT_ID')
REDDIT_CLIENT_SECRET = os.getenv('REDDIT_CLIENT_SECRET')
REDDIT_USER_AGENT = os.getenv('REDDIT_USER_AGENT', 'AbsurdityIndexCollector/1.0')

# Subreddits to collect from
SUBREDDITS = [
    'FirstTimeHomeBuyer',
    'RealEstate',
    'povertyfinance',
    'lostgeneration',
    'renters',
    'HousingCrisis',
    'personalfinance'
]

# Search queries within subreddits
SEARCH_QUERIES = [
    "can't afford house",
    "priced out",
    "gave up on homeownership",
    "rent increase",
    "eviction",
    "down payment impossible",
    "housing crisis",
    "landlord"
]

# Core housing keywords that MUST be present to avoid false positives
HOUSING_REQUIRED_KEYWORDS = [
    'housing', 'house', 'home', 'apartment', 'rent', 'renting', 'rental',
    'landlord', 'evict', 'eviction', 'mortgage', 'homeowner', 'homeownership',
    'real estate', 'property', 'market', 'afford', 'down payment',
    'homeless', 'housing crisis', 'foreclosure', 'lease'
]

# Level 3: Crisis - Housing insecurity, gave up entirely
LEVEL_3_KEYWORDS = [
    'evicted', 'eviction', 'homeless', 'living in car',
    'couch surfing', 'lost apartment', 'foreclosure',
    "can't pay rent", 'behind on rent',
    'gave up on homeownership', 'will never own', 'homeownership impossible',
    'accepted i will never', 'dream is dead', 'given up on buying',
    'living with parents', 'moved back home', 'multi-generational',
    'forced to relocate', 'priced out of city', 'left my hometown',
    'depressed about housing', 'anxiety about rent', 'panic',
    'hopeless', 'breaking point', 'suicidal'
]

# Level 2: Frustrated - Can't buy, rent struggles
LEVEL_2_KEYWORDS = [
    "can't save for down payment", 'down payment impossible',
    "can't afford house", 'priced out', 'outbid',
    'lost bidding war', 'housing too expensive',
    'rent increase', 'rent went up', 'landlord raised rent',
    "can't afford rent increase", 'rent is 50%',
    'paycheck goes to rent', 'nothing left after rent',
    'smaller apartment', 'worse neighborhood', 'longer commute',
    'roommates at 30', 'roommates at 40', 'shared housing',
    'housing market broken', 'system is rigged', 'investors ruining',
    'corporations buying homes', 'private equity', 'wall street landlords'
]

def is_housing_related(title, text):
    """
    Validate that post is actually about housing (not false positive)
    """
    content = (title + " " + text).lower()
    return any(keyword in content for keyword in HOUSING_REQUIRED_KEYWORDS)

def categorize_post(title, text):
    """
    Categorize post into Level 1/2/3 based on crisis language
    Returns None if not housing-related
    """
    # First check: Is this actually about housing?
    if not is_housing_related(title, text):
        return None

    content = (title + " " + text).lower()

    # Count Level 3 keywords (crisis/housing insecurity)
    level_3_count = sum(1 for keyword in LEVEL_3_KEYWORDS if keyword in content)

    # Level 3: Crisis
    if level_3_count >= 2 or any(phrase in content for phrase in [
        'evicted', 'eviction', 'homeless', 'living in car',
        'gave up on homeownership', 'will never own', 'dream is dead',
        'living with parents', 'moved back home', 'hopeless', 'suicidal'
    ]):
        return 'LEVEL_3_CRISIS'

    # Count Level 2 keywords (frustrated but still trying)
    level_2_count = sum(1 for keyword in LEVEL_2_KEYWORDS if keyword in content)

    # Level 2: Frustrated
    if level_2_count >= 2 or any(phrase in content for phrase in [
        "can't afford", 'priced out', 'down payment impossible',
        'rent increase', 'landlord raised rent', 'housing market broken'
    ]):
        return 'LEVEL_2_FRUSTRATED'

    # Level 1: Mild awareness
    return 'LEVEL_1_AWARE'

def collect_from_subreddit(reddit, subreddit_name, posts_per_subreddit=30):
    """Collect recent posts from a subreddit (last 90 days)"""
    posts = []

    try:
        subreddit = reddit.subreddit(subreddit_name)

        # Calculate 90 days ago timestamp
        from datetime import timedelta
        ninety_days_ago = datetime.now() - timedelta(days=90)
        ninety_days_timestamp = ninety_days_ago.timestamp()

        # Get recent posts (mix of hot and new from last 90 days)
        submissions_collected = 0
        for submission in subreddit.new(limit=posts_per_subreddit * 3):  # Get more to filter by date
            # Only include posts from last 90 days
            if submission.created_utc < ninety_days_timestamp:
                continue

            submissions_collected += 1
            if submissions_collected > posts_per_subreddit:
                break
            # Skip stickied posts
            if submission.stickied:
                continue

            title = submission.title
            text = submission.selftext

            # Categorize
            category = categorize_post(title, text)

            # Skip if not housing-related
            if category is None:
                continue

            # Find crisis keywords
            content_lower = (title + " " + text).lower()
            found_level_3 = [kw for kw in LEVEL_3_KEYWORDS if kw in content_lower]
            found_level_2 = [kw for kw in LEVEL_2_KEYWORDS if kw in content_lower]
            found_keywords = found_level_3 + found_level_2

            posts.append({
                'subreddit': f'r/{subreddit_name}',
                'post_id': submission.id,
                'url': f'https://reddit.com{submission.permalink}',
                'title': title,
                'text_snippet': text[:300] if text else '',
                'score': submission.score,
                'num_comments': submission.num_comments,
                'created_date': datetime.fromtimestamp(submission.created_utc).strftime('%Y-%m-%d'),
                'crisis_keywords': ', '.join(found_keywords[:5]),
                'category': category
            })

        print(f"  ✓ Collected {len(posts)} housing-related posts from r/{subreddit_name}")
        return posts

    except Exception as e:
        print(f"  ✗ Error collecting from r/{subreddit_name}: {e}")
        return []

def main():
    """Main execution"""
    print("=" * 70)
    print("HOUSING DESPAIR REDDIT POST COLLECTOR")
    print("=" * 70)

    # Check API credentials
    if not REDDIT_CLIENT_ID or not REDDIT_CLIENT_SECRET:
        print("\n❌ ERROR: Reddit API credentials not found!")
        print("\nYou need to set up Reddit API access:")
        print("1. Go to https://www.reddit.com/prefs/apps")
        print("2. Click 'create another app...' at bottom")
        print("3. Fill out:")
        print("   - name: Absurdity Index Collector")
        print("   - type: script")
        print("   - redirect uri: http://localhost:8080")
        print("4. Click 'create app'")
        print("5. Copy the client ID (under 'personal use script')")
        print("6. Copy the secret")
        print("\nThen add to .env file:")
        print("REDDIT_CLIENT_ID=your_client_id_here")
        print("REDDIT_CLIENT_SECRET=your_secret_here")
        print("REDDIT_USER_AGENT=AbsurdityIndexCollector/1.0")
        return

    # Initialize Reddit API
    try:
        reddit = praw.Reddit(
            client_id=REDDIT_CLIENT_ID,
            client_secret=REDDIT_CLIENT_SECRET,
            user_agent=REDDIT_USER_AGENT
        )
        print(f"\n✓ Connected to Reddit API")
    except Exception as e:
        print(f"\n✗ Failed to connect to Reddit API: {e}")
        return

    all_posts = []

    # Collect from each subreddit
    posts_per_sub = 30  # Aim for ~200 total posts
    for subreddit_name in SUBREDDITS:
        print(f"\nCollecting from r/{subreddit_name}...")
        posts = collect_from_subreddit(reddit, subreddit_name, posts_per_sub)
        all_posts.extend(posts)

    # Convert to DataFrame
    df = pd.DataFrame(all_posts)

    # Remove duplicates
    df_unique = df.drop_duplicates(subset=['post_id'])

    # Save to CSV
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_dir = 'data-collection/collected-data'
    os.makedirs(output_dir, exist_ok=True)
    output_file = f'{output_dir}/housing_despair_reddit_{timestamp}.csv'
    df_unique.to_csv(output_file, index=False)

    print("\n" + "=" * 70)
    print(f"RESULTS SAVED: {output_file}")
    print("=" * 70)
    print(f"\nTotal posts collected: {len(df)}")
    print(f"Unique posts (after deduplication): {len(df_unique)}")

    if len(df_unique) > 0:
        print(f"\nBreakdown by category:")
        print(df_unique['category'].value_counts())

        # Calculate crisis ratio
        total = len(df_unique)
        level_3 = len(df_unique[df_unique['category'] == 'LEVEL_3_CRISIS'])
        level_2 = len(df_unique[df_unique['category'] == 'LEVEL_2_FRUSTRATED'])
        level_1 = len(df_unique[df_unique['category'] == 'LEVEL_1_AWARE'])

        print(f"\nLevel 1 (Aware): {level_1} ({level_1/total*100:.1f}%)")
        print(f"Level 2 (Frustrated): {level_2} ({level_2/total*100:.1f}%)")
        print(f"Level 3 (Crisis): {level_3} ({level_3/total*100:.1f}%)")
        print(f"\nCrisis ratio (Level 3 only): {level_3/total*100:.1f}%")

        # Top posts by engagement
        print(f"\n\nTOP 5 MOST-ENGAGED POSTS:")
        print("-" * 70)
        top_5 = df_unique.nlargest(5, 'score')[['title', 'score', 'num_comments', 'category', 'url']]
        for idx, row in top_5.iterrows():
            print(f"\n{row['title']}")
            print(f"  Score: {row['score']:,} | Comments: {row['num_comments']:,} | Category: {row['category']}")
            print(f"  {row['url']}")

if __name__ == '__main__':
    main()
