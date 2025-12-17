#!/usr/bin/env python3
"""
Reddit AI Psychosis Data Collection
Samples posts from r/CharacterAI and r/replika to measure parasocial AI dependency

SETUP REQUIRED:
1. Create Reddit app at: https://www.reddit.com/prefs/apps
2. Create .env file with:
   REDDIT_CLIENT_ID=your_client_id
   REDDIT_CLIENT_SECRET=your_client_secret
   REDDIT_USER_AGENT=DisappointmentsDashboard/1.0
"""

import praw
import pandas as pd
from datetime import datetime
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize Reddit API
reddit = praw.Reddit(
    client_id=os.getenv('REDDIT_CLIENT_ID', 'temp'),
    client_secret=os.getenv('REDDIT_CLIENT_SECRET', 'temp'),
    user_agent=os.getenv('REDDIT_USER_AGENT', 'DisappointmentsDashboard/1.0'),
    check_for_async=False
)

# Subreddits to monitor
subreddits = ['CharacterAI', 'replika']

# Keywords indicating potential crisis-level dependency
crisis_keywords = [
    'love', 'addiction', 'addicted', 'breakup', 'broke up',
    'depressed', 'depression', 'grief', 'crying', 'suicide',
    'only friend', 'replacing', 'prefer', 'real relationship',
    "can't stop", 'obsessed', 'therapy', 'help me', 'worried'
]

print("="*70)
print("Reddit AI Psychosis Data Collection")
print("="*70)
print(f"Subreddits: {', '.join(subreddits)}")
print(f"Target sample: 100 posts per subreddit = 200 total")
print(f"Crisis keywords: {len(crisis_keywords)} tracked")
print("="*70)

all_posts = []

for subreddit_name in subreddits:
    print(f"\n📊 Collecting from r/{subreddit_name}...")

    try:
        subreddit = reddit.subreddit(subreddit_name)

        # Get mix of hot, new, and top posts
        posts_hot = list(subreddit.hot(limit=40))
        posts_new = list(subreddit.new(limit=40))
        posts_top = list(subreddit.top('week', limit=20))

        all_sub_posts = posts_hot + posts_new + posts_top

        # Deduplicate by post ID
        seen_ids = set()
        unique_posts = []
        for post in all_sub_posts:
            if post.id not in seen_ids:
                seen_ids.add(post.id)
                unique_posts.append(post)

        # Take first 100 unique
        posts_to_analyze = unique_posts[:100]

        print(f"   Collected {len(posts_to_analyze)} posts")

        for post in posts_to_analyze:
            # Extract post data
            post_data = {
                'subreddit': subreddit_name,
                'post_id': post.id,
                'title': post.title,
                'selftext': post.selftext[:500] if post.selftext else '',  # First 500 chars
                'score': post.score,
                'num_comments': post.num_comments,
                'created_utc': datetime.fromtimestamp(post.created_utc),
                'url': f"https://reddit.com{post.permalink}",
                'author': str(post.author),
            }

            # Check for crisis keywords in title + text
            text_to_check = (post.title + ' ' + post.selftext).lower()
            matching_keywords = [kw for kw in crisis_keywords if kw in text_to_check]

            post_data['crisis_keywords_found'] = ', '.join(matching_keywords) if matching_keywords else 'none'
            post_data['crisis_keyword_count'] = len(matching_keywords)

            # Manual categorization placeholder
            post_data['category'] = 'TO_REVIEW'  # Will be: Level1, Level2, Level3
            post_data['notes'] = ''

            all_posts.append(post_data)

    except Exception as e:
        print(f"   ⚠️  Error collecting from r/{subreddit_name}: {e}")
        continue

# Create DataFrame
df = pd.DataFrame(all_posts)

print("\n" + "="*70)
print("COLLECTION SUMMARY")
print("="*70)
print(f"Total posts collected: {len(df)}")
print(f"From r/CharacterAI: {len(df[df['subreddit'] == 'CharacterAI'])}")
print(f"From r/replika: {len(df[df['subreddit'] == 'replika'])}")
print(f"\nPosts with crisis keywords: {len(df[df['crisis_keyword_count'] > 0])}")
print(f"Posts with 3+ crisis keywords: {len(df[df['crisis_keyword_count'] >= 3])}")

# Show top crisis keyword mentions
if len(df) > 0:
    print("\nMost common crisis keywords:")
    all_keywords = []
    for keywords_str in df['crisis_keywords_found']:
        if keywords_str != 'none':
            all_keywords.extend(keywords_str.split(', '))

    if all_keywords:
        from collections import Counter
        keyword_counts = Counter(all_keywords)
        for keyword, count in keyword_counts.most_common(10):
            print(f"  {keyword}: {count}")

# Save to CSV
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
filename = f"reddit_ai_psychosis_{timestamp}.csv"
df.to_csv(filename, index=False)

print(f"\n✅ Saved to: {filename}")
print("\nNEXT STEPS:")
print("1. Open CSV in spreadsheet")
print("2. Review posts marked 'TO_REVIEW'")
print("3. Categorize each as:")
print("   - Level1: Casual AI use, no dependency")
print("   - Level2: Emotional dependency, yellow flag")
print("   - Level3: Crisis-level attachment, red flag")
print("4. Count Level2 + Level3 to calculate crisis ratio")
print("="*70)
