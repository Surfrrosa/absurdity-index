#!/usr/bin/env python3
"""
Integrate Reddit Data into Absurdity Index Metrics
Updates metricDetailData.ts with Reddit crisis ratios and sample posts
"""

import json
import csv
from datetime import datetime
from pathlib import Path

# Reddit data we collected
REDDIT_DATA = {
    "What Healthcare?": {
        "posts": 141,
        "level_1": 100,
        "level_2": 35,
        "level_3": 6,
        "crisis_ratio": 29.1,
        "csv_file": "healthcare_reddit_20251222_124041.csv"
    },
    "AI Psychosis": {
        "posts": 290,
        "level_1": 225,
        "level_2": 37,
        "level_3": 28,
        "crisis_ratio": 22.4,
        "csv_file": "ai_psychosis_reddit_20251222_144733.csv"
    },
    "Subscription Overload": {
        "posts": 37,
        "level_1": 32,
        "level_2": 5,
        "level_3": 0,
        "crisis_ratio": 13.5,
        "csv_file": "subscription_overload_reddit_20251222_135823.csv"
    },
    "Wage Stagnation": {
        "posts": 128,
        "level_1": 100,
        "level_2": 22,
        "level_3": 6,
        "crisis_ratio": 21.9,
        "csv_file": "wage_stagnation_reddit_20251222_135920.csv"
    },
    "Housing Despair": {
        "posts": 169,
        "level_1": 119,
        "level_2": 34,
        "level_3": 16,
        "crisis_ratio": 29.6,
        "csv_file": "housing_despair_reddit_20251222_144453.csv"
    },
    "Dating App Despair": {
        "posts": 86,
        "level_1": 57,
        "level_2": 29,
        "level_3": 0,
        "crisis_ratio": 33.7,
        "csv_file": "dating_app_despair_reddit_20251222_140055.csv"
    },
    "Layoff Watch": {
        "posts": 106,
        "level_1": 61,
        "level_2": 43,
        "level_3": 2,
        "crisis_ratio": 42.5,
        "csv_file": "layoff_watch_reddit_20251222_140133.csv"
    },
    "Airline Chaos": {
        "posts": 47,
        "level_1": 30,
        "level_2": 15,
        "level_3": 2,
        "crisis_ratio": 36.2,
        "csv_file": "airline_chaos_reddit_20251222_140211.csv"
    }
}

def load_sample_posts(csv_file, limit=3):
    """Load sample Reddit posts from CSV"""
    csv_path = Path("collected-data") / csv_file
    if not csv_path.exists():
        return []

    samples = []
    with open(csv_path, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        posts = list(reader)

        # Get mix of Level 3, 2, and 1
        level_3 = [p for p in posts if 'LEVEL_3' in p['category']]
        level_2 = [p for p in posts if 'LEVEL_2' in p['category']]
        level_1 = [p for p in posts if 'LEVEL_1' in p['category']]

        # Take top by score (upvotes)
        level_3_sorted = sorted(level_3, key=lambda x: int(x.get('score', 0)), reverse=True)
        level_2_sorted = sorted(level_2, key=lambda x: int(x.get('score', 0)), reverse=True)
        level_1_sorted = sorted(level_1, key=lambda x: int(x.get('score', 0)), reverse=True)

        # Take 1 from each level if available
        for post in (level_3_sorted[:1] + level_2_sorted[:1] + level_1_sorted[:1]):
            level = 3 if 'LEVEL_3' in post['category'] else 2 if 'LEVEL_2' in post['category'] else 1
            samples.append({
                "content": post['title'][:100],
                "platform": "reddit",
                "level": level,
                "date": post['created_date'],
                "url": post['url'],
                "score": int(post.get('score', 0)),
                "subreddit": post.get('subreddit', '')
            })

    return samples[:limit]

def calculate_blended_crisis_ratio(youtube_cr, reddit_cr):
    """Blend YouTube and Reddit crisis ratios with equal weighting"""
    return (youtube_cr + reddit_cr) / 2

def calculate_new_score(official_score, blended_social_cr):
    """
    Calculate new final score: 40% official, 60% social sentiment
    Social sentiment is normalized crisis ratio
    """
    social_score = blended_social_cr  # Already a 0-100 scale
    return (official_score * 0.4) + (social_score * 0.6)

def main():
    print("=" * 80)
    print("INTEGRATING REDDIT DATA INTO ABSURDITY INDEX")
    print("=" * 80)

    # Calculate updates for each metric
    updates = {}

    for metric_name, reddit_data in REDDIT_DATA.items():
        print(f"\n📊 {metric_name}")
        print(f"  Reddit: {reddit_data['posts']} posts, {reddit_data['crisis_ratio']}% crisis")

        # Load sample posts
        samples = load_sample_posts(reddit_data['csv_file'], limit=2)
        print(f"  Loaded {len(samples)} sample posts")

        updates[metric_name] = {
            "reddit_posts": reddit_data['posts'],
            "reddit_l1": reddit_data['level_1'],
            "reddit_l2": reddit_data['level_2'],
            "reddit_l3": reddit_data['level_3'],
            "reddit_crisis_ratio": reddit_data['crisis_ratio'],
            "sample_posts": samples
        }

    # Print summary
    print("\n" + "=" * 80)
    print("REDDIT DATA SUMMARY")
    print("=" * 80)
    print(f"Total Posts Collected: {sum(d['posts'] for d in REDDIT_DATA.values())}")
    print(f"Metrics Updated: {len(REDDIT_DATA)}")

    print("\n📈 Crisis Ratio Comparison:")
    print(f"{'Metric':<25} {'Reddit CR':<12} {'Status'}")
    print("-" * 50)
    for metric, data in REDDIT_DATA.items():
        cr = data['crisis_ratio']
        status = "🔴 High" if cr > 35 else "🟡 Medium" if cr > 20 else "🟢 Low"
        print(f"{metric:<25} {cr:>6.1f}%      {status}")

    # Save update data to JSON for TypeScript integration
    output_file = "reddit-integration-data.json"
    with open(output_file, 'w') as f:
        json.dump(updates, f, indent=2)

    print(f"\n✅ Integration data saved to: {output_file}")
    print("\nNext step: Update metricDetailData.ts with this data")
    print("=" * 80)

if __name__ == '__main__':
    main()
