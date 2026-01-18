#!/usr/bin/env python3
"""
Cross-Metric Reddit Post Deduplication Script

This script ensures each Reddit post appears in only ONE metric by:
1. Scanning all Reddit CSV files for duplicate post IDs
2. Scoring each post against each metric's keywords
3. Assigning the post to the single best-fit metric
4. Removing it from other metrics' CSVs

Run this AFTER all Reddit collectors finish, BEFORE update_metric_data.py

Usage:
    python deduplicate_reddit_posts.py
"""

import os
import csv
import glob
from datetime import datetime
from collections import defaultdict

# Change to script directory
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
os.chdir(SCRIPT_DIR)

DATA_DIR = 'collected-data'

# Metric slug patterns for CSV files
METRIC_PATTERNS = {
    'healthcare': 'healthcare_reddit_*.csv',
    'ai_psychosis': 'ai_psychosis_reddit_*.csv',
    'subscription_overload': 'subscription_overload_reddit_*.csv',
    'wage_stagnation': 'wage_stagnation_reddit_*.csv',
    'housing_despair': 'housing_despair_reddit_*.csv',
    'dating_app_despair': 'dating_app_despair_reddit_*.csv',
    'layoff_watch': 'layoff_watch_reddit_*.csv',
    'airline_chaos': 'airline_chaos_reddit_*.csv',
}

# Primary keywords for each metric - used to score posts for best fit
# Higher score = better match for that metric
METRIC_KEYWORDS = {
    'healthcare': [
        'insurance', 'medical', 'hospital', 'doctor', 'treatment', 'diagnosis',
        'prescription', 'medication', 'medicine', 'healthcare', 'health care',
        'denied claim', 'prior authorization', 'copay', 'deductible', 'premium',
        'surgery', 'cancer', 'chronic', 'illness', 'sick', 'disease',
        'emergency room', 'er visit', 'ambulance', 'medical bill', 'medical debt'
    ],
    'ai_psychosis': [
        'ai', 'chatgpt', 'replika', 'character.ai', 'character ai', 'chatbot',
        'artificial intelligence', 'gpt', 'bot', 'ai companion', 'ai girlfriend',
        'ai boyfriend', 'ai friend', 'virtual', 'digital companion'
    ],
    'subscription_overload': [
        'subscription', 'streaming', 'netflix', 'hulu', 'disney', 'hbo', 'max',
        'spotify', 'apple music', 'amazon prime', 'monthly fee', 'annual fee',
        'cancel subscription', 'too many subscriptions', 'subscription fatigue',
        'streaming service', 'subscribe', 'membership'
    ],
    'wage_stagnation': [
        'wage', 'salary', 'paycheck', 'pay', 'income', 'hourly', 'minimum wage',
        'raise', 'promotion', 'cost of living', 'inflation', 'afford',
        'paycheck to paycheck', 'living paycheck', 'broke', 'poor', 'poverty',
        'bills', 'expenses', 'budget', 'financial', 'money', 'debt',
        'work', 'job', 'employer', 'boss', 'overtime', 'side hustle'
    ],
    'housing_despair': [
        'rent', 'rental', 'landlord', 'tenant', 'lease', 'apartment', 'house',
        'home', 'housing', 'mortgage', 'down payment', 'homeowner', 'eviction',
        'evicted', 'roommate', 'living situation', 'move out', 'kicked out',
        'homeless', 'van life', 'couch surfing', 'real estate', 'property',
        'buy a home', 'priced out', 'afford rent', 'rent increase'
    ],
    'dating_app_despair': [
        'dating', 'tinder', 'hinge', 'bumble', 'match', 'swipe', 'online dating',
        'dating app', 'relationship', 'single', 'ghosted', 'matched', 'date',
        'boyfriend', 'girlfriend', 'romance', 'love life', 'dating scene'
    ],
    'layoff_watch': [
        'layoff', 'laid off', 'fired', 'terminated', 'let go', 'downsized',
        'unemployment', 'unemployed', 'job search', 'job hunting', 'resume',
        'interview', 'application', 'hiring', 'recruiter', 'job market',
        'severance', 'career', 'position eliminated'
    ],
    'airline_chaos': [
        'flight', 'airline', 'airport', 'plane', 'travel', 'flying', 'flew',
        'cancelled', 'delayed', 'luggage', 'baggage', 'passenger', 'boarding',
        'gate', 'terminal', 'pilot', 'crew', 'turbulence', 'layover',
        'connection', 'ticket', 'booking'
    ]
}


def get_latest_csv(pattern):
    """Get the most recent CSV file matching the pattern."""
    files = glob.glob(os.path.join(DATA_DIR, pattern))
    if not files:
        return None
    return max(files, key=os.path.getmtime)


def read_csv_posts(filepath):
    """Read posts from a CSV file, return list of dicts with post_id as key identifier."""
    posts = []
    if not filepath or not os.path.exists(filepath):
        return posts

    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                posts.append(row)
    except Exception as e:
        print(f"  Error reading {filepath}: {e}")

    return posts


def write_csv_posts(filepath, posts, fieldnames):
    """Write posts back to CSV file."""
    try:
        with open(filepath, 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(posts)
        return True
    except Exception as e:
        print(f"  Error writing {filepath}: {e}")
        return False


def score_post_for_metric(post, metric):
    """
    Score how well a post matches a metric based on keyword presence.
    Returns an integer score (higher = better match).
    """
    keywords = METRIC_KEYWORDS.get(metric, [])
    if not keywords:
        return 0

    # Combine title and text for matching
    title = post.get('title', '').lower()
    text = post.get('selftext_snippet', post.get('selftext', '')).lower()
    combined = title + ' ' + text

    score = 0
    for keyword in keywords:
        if keyword in combined:
            # Title matches worth more
            if keyword in title:
                score += 3
            else:
                score += 1

    return score


def find_best_metric(post, current_metrics):
    """
    Given a post that appears in multiple metrics, determine the best fit.
    Returns the metric name that's the best match.
    """
    scores = {}
    for metric in current_metrics:
        scores[metric] = score_post_for_metric(post, metric)

    # Return metric with highest score
    # If tie, prefer the first one alphabetically for consistency
    best_metric = max(scores.keys(), key=lambda m: (scores[m], -ord(m[0])))
    return best_metric, scores


def main():
    print("=" * 80)
    print("CROSS-METRIC REDDIT POST DEDUPLICATION")
    print(f"Started: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 80)

    # Step 1: Load all posts from all metrics
    print("\n[1/4] Loading posts from all metrics...")

    all_posts = {}  # metric -> list of posts
    csv_files = {}  # metric -> filepath
    fieldnames = {}  # metric -> CSV fieldnames

    for metric, pattern in METRIC_PATTERNS.items():
        filepath = get_latest_csv(pattern)
        if filepath:
            posts = read_csv_posts(filepath)
            all_posts[metric] = posts
            csv_files[metric] = filepath

            # Store fieldnames from first post
            if posts:
                fieldnames[metric] = list(posts[0].keys())

            print(f"  {metric}: {len(posts)} posts from {os.path.basename(filepath)}")
        else:
            all_posts[metric] = []
            print(f"  {metric}: No CSV found")

    # Step 2: Build index of post_id -> metrics
    print("\n[2/4] Building duplicate index...")

    post_index = defaultdict(list)  # post_id -> [(metric, post_data), ...]

    for metric, posts in all_posts.items():
        for post in posts:
            post_id = post.get('post_id', '')
            if post_id:
                post_index[post_id].append((metric, post))

    # Find duplicates
    duplicates = {pid: metrics for pid, metrics in post_index.items() if len(metrics) > 1}

    print(f"  Total unique post IDs: {len(post_index)}")
    print(f"  Posts appearing in multiple metrics: {len(duplicates)}")

    if not duplicates:
        print("\n  No duplicates found! Nothing to do.")
        return

    # Step 3: Assign each duplicate to best metric
    print("\n[3/4] Assigning duplicates to best-fit metrics...")

    reassignments = []  # List of (post_id, title, from_metrics, to_metric)
    posts_to_remove = defaultdict(set)  # metric -> set of post_ids to remove

    for post_id, metric_posts in duplicates.items():
        metrics = [m for m, p in metric_posts]
        post_data = metric_posts[0][1]  # Use first post's data for scoring

        best_metric, scores = find_best_metric(post_data, metrics)

        # Mark for removal from non-best metrics
        for metric, _ in metric_posts:
            if metric != best_metric:
                posts_to_remove[metric].add(post_id)

        title = post_data.get('title', '')[:60]
        reassignments.append({
            'post_id': post_id,
            'title': title,
            'from_metrics': [m for m in metrics if m != best_metric],
            'to_metric': best_metric,
            'scores': scores
        })

    # Print reassignment report
    print(f"\n  Reassignment Summary:")
    for r in reassignments[:10]:  # Show first 10
        from_str = ', '.join(r['from_metrics'])
        print(f"    '{r['title']}...'")
        print(f"      KEEP in {r['to_metric']} (score: {r['scores'][r['to_metric']]})")
        print(f"      REMOVE from: {from_str}")

    if len(reassignments) > 10:
        print(f"    ... and {len(reassignments) - 10} more")

    # Step 4: Update CSV files
    print("\n[4/4] Updating CSV files...")

    for metric, remove_ids in posts_to_remove.items():
        if not remove_ids:
            continue

        filepath = csv_files.get(metric)
        if not filepath:
            continue

        original_count = len(all_posts[metric])
        filtered_posts = [p for p in all_posts[metric] if p.get('post_id') not in remove_ids]
        new_count = len(filtered_posts)

        if fieldnames.get(metric):
            success = write_csv_posts(filepath, filtered_posts, fieldnames[metric])
            if success:
                print(f"  {metric}: {original_count} -> {new_count} (removed {len(remove_ids)})")
            else:
                print(f"  {metric}: FAILED to update")

    # Final summary
    print("\n" + "=" * 80)
    print("DEDUPLICATION COMPLETE")
    print("=" * 80)
    print(f"\nTotal duplicates resolved: {len(duplicates)}")
    print(f"Posts reassigned to better-fit metrics: {len(reassignments)}")

    # Show by-metric summary
    print("\nRemovals by metric:")
    for metric in sorted(posts_to_remove.keys()):
        count = len(posts_to_remove[metric])
        if count > 0:
            print(f"  {metric}: -{count} posts")

    print("\n" + "=" * 80)


if __name__ == '__main__':
    main()
