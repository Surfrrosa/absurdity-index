#!/usr/bin/env python3
"""
Auto-update sampleData arrays in metricDetailData.ts from collected data.

This script:
1. Reads the latest collected data for each metric (YouTube, Reddit, TikTok)
2. Selects representative samples (mix of severity levels and platforms)
3. Updates the sampleData arrays in metricDetailData.ts

Run this AFTER data collection, BEFORE or AFTER update_metric_data.py

Usage:
    python update_sample_data.py
"""

import os
import csv
import glob
import re
import json
from datetime import datetime

# Change to script directory
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
os.chdir(SCRIPT_DIR)

DATA_DIR = 'collected-data'
METRIC_DATA_FILE = '../lib/metricDetailData.ts'

# Metric configurations
METRICS = {
    'What Healthcare?': {
        'youtube_pattern': 'healthcare_youtube_*.csv',
        'reddit_pattern': 'healthcare_reddit_*.csv',
        'tiktok_metric': 'healthcare'
    },
    'AI Psychosis': {
        'youtube_pattern': 'ai_psychosis_youtube_*.csv',
        'reddit_pattern': 'ai_psychosis_reddit_*.csv',
        'tiktok_metric': 'ai_psychosis'
    },
    'Subscription Overload': {
        'youtube_pattern': 'subscription_overload_youtube_*.csv',
        'reddit_pattern': 'subscription_overload_reddit_*.csv',
        'tiktok_metric': 'subscription_overload'
    },
    'Wage Stagnation': {
        'youtube_pattern': 'wage_stagnation_youtube_*.csv',
        'reddit_pattern': 'wage_stagnation_reddit_*.csv',
        'tiktok_metric': 'wage_stagnation'
    },
    'Housing Despair': {
        'youtube_pattern': 'housing_despair_youtube_*.csv',
        'reddit_pattern': 'housing_despair_reddit_*.csv',
        'tiktok_metric': 'housing_despair'
    },
    'Dating App Despair': {
        'youtube_pattern': 'dating_app_despair_youtube_*.csv',
        'reddit_pattern': 'dating_app_despair_reddit_*.csv',
        'tiktok_metric': 'dating_app_despair'
    },
    'Layoff Watch': {
        'youtube_pattern': 'layoff_watch_youtube_*.csv',
        'reddit_pattern': 'layoff_watch_reddit_*.csv',
        'tiktok_metric': 'layoff_watch'
    },
    'Airline Chaos': {
        'youtube_pattern': 'airline_chaos_youtube_*.csv',
        'reddit_pattern': 'airline_chaos_reddit_*.csv',
        'tiktok_metric': 'airline_chaos'
    }
}

# TikTok combined file pattern
TIKTOK_PATTERN = 'tiktok_youtube_*.csv'


def get_latest_file(pattern):
    """Get the most recent file matching the pattern."""
    files = glob.glob(os.path.join(DATA_DIR, pattern))
    if not files:
        return None
    return max(files, key=os.path.getmtime)


def read_csv_data(filepath):
    """Read CSV file and return list of dicts."""
    if not filepath or not os.path.exists(filepath):
        return []

    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            return list(csv.DictReader(f))
    except Exception as e:
        print(f"  Error reading {filepath}: {e}")
        return []


def get_level_from_category(category):
    """Convert category string to level number."""
    if not category:
        return 1
    category = category.upper()
    if 'LEVEL_3' in category or 'CRISIS' in category:
        return 3
    elif 'LEVEL_2' in category:
        return 2
    return 1


def select_youtube_samples(data, max_samples=2):
    """Select representative YouTube samples."""
    if not data:
        return []

    # Sort by view count (highest engagement)
    sorted_data = sorted(data, key=lambda x: int(x.get('view_count', 0) or 0), reverse=True)

    samples = []
    seen_levels = set()

    # Try to get diverse levels
    for row in sorted_data:
        category = row.get('category', '')
        level = get_level_from_category(category)

        # Prefer getting different levels
        if level not in seen_levels or len(samples) < max_samples:
            title = row.get('title', '')[:100]
            if not title:
                continue

            samples.append({
                'content': title,
                'platform': 'youtube',
                'level': level,
                'date': row.get('published_date', row.get('published', ''))[:10],
                'url': row.get('url', ''),
                'videoId': row.get('video_id', ''),
                'viewCount': int(row.get('view_count', 0) or 0),
                'commentCount': int(row.get('comment_count', row.get('comments', 0)) or 0)
            })
            seen_levels.add(level)

            if len(samples) >= max_samples:
                break

    return samples


def select_reddit_samples(data, max_samples=2):
    """Select representative Reddit samples."""
    if not data:
        return []

    # Sort by score (highest engagement)
    sorted_data = sorted(data, key=lambda x: int(x.get('score', 0) or 0), reverse=True)

    samples = []
    seen_levels = set()

    for row in sorted_data:
        category = row.get('category', '')
        level = get_level_from_category(category)

        if level not in seen_levels or len(samples) < max_samples:
            title = row.get('title', '')[:100]
            if not title:
                continue

            samples.append({
                'content': title,
                'platform': 'reddit',
                'level': level,
                'date': row.get('created_date', '')[:10],
                'url': row.get('url', '')
            })
            seen_levels.add(level)

            if len(samples) >= max_samples:
                break

    return samples


def select_tiktok_samples(all_tiktok_data, metric_name, max_samples=1):
    """Select TikTok samples for a specific metric."""
    if not all_tiktok_data:
        return []

    # Filter for this metric
    metric_data = [r for r in all_tiktok_data if r.get('metric', '') == metric_name]

    if not metric_data:
        return []

    # Sort by views
    sorted_data = sorted(metric_data, key=lambda x: int(x.get('views', 0) or 0), reverse=True)

    samples = []
    for row in sorted_data[:max_samples]:
        title = row.get('title', '')[:100]
        if not title:
            continue

        samples.append({
            'content': title,
            'platform': 'tiktok',
            'level': get_level_from_category(row.get('category', '')),
            'date': row.get('published', '')[:10],
            'url': row.get('url', ''),
            'videoId': row.get('video_id', ''),
            'viewCount': int(row.get('views', 0) or 0)
        })

    return samples


def format_sample_for_ts(sample):
    """Format a sample dict as TypeScript object string."""
    lines = ['      {']

    # Content (escape quotes)
    content = sample.get('content', '').replace('"', '\\"')
    lines.append(f'        content: "{content}",')
    lines.append(f'        platform: "{sample.get("platform", "")}",')
    lines.append(f'        level: {sample.get("level", 1)},')
    lines.append(f'        date: "{sample.get("date", "")}",')
    lines.append(f'        url: "{sample.get("url", "")}"')

    # Optional fields for YouTube/TikTok
    if sample.get('videoId'):
        # Remove last line's comma handling
        lines[-1] = lines[-1][:-1] + ','  # Add comma to url line
        lines.append(f'        videoId: "{sample.get("videoId")}",')
        lines.append(f'        viewCount: {sample.get("viewCount", 0)},')
        lines.append(f'        commentCount: {sample.get("commentCount", 0)}')

    lines.append('      }')
    return '\n'.join(lines)


def update_metric_samples(content, metric_name, samples):
    """Update the sampleData array for a metric in the TypeScript content."""
    if not samples:
        return content

    # Format samples as TypeScript
    samples_ts = ',\n'.join(format_sample_for_ts(s) for s in samples)

    # Pattern to find and replace sampleData for this metric
    # This is tricky because we need to find the right metric section
    pattern = rf'("{re.escape(metric_name)}": \{{[^}}]*?sampleData: \[)[^\]]*(\])'

    def replacer(match):
        return f'{match.group(1)}\n{samples_ts}\n    {match.group(2)}'

    new_content = re.sub(pattern, replacer, content, flags=re.DOTALL)

    return new_content


def main():
    print("=" * 80)
    print("AUTO-UPDATE SAMPLE DATA")
    print(f"Started: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 80)

    # Read current TypeScript file
    with open(METRIC_DATA_FILE, 'r', encoding='utf-8') as f:
        content = f.read()

    # Load TikTok data once (combined file)
    tiktok_file = get_latest_file(TIKTOK_PATTERN)
    all_tiktok_data = read_csv_data(tiktok_file) if tiktok_file else []
    print(f"\nLoaded {len(all_tiktok_data)} TikTok entries")

    # Process each metric
    for metric_name, config in METRICS.items():
        print(f"\n{metric_name}:")

        # Get latest data files
        youtube_file = get_latest_file(config['youtube_pattern'])
        reddit_file = get_latest_file(config['reddit_pattern'])

        youtube_data = read_csv_data(youtube_file) if youtube_file else []
        reddit_data = read_csv_data(reddit_file) if reddit_file else []

        print(f"  YouTube: {len(youtube_data)} entries")
        print(f"  Reddit: {len(reddit_data)} entries")

        # Select samples (2 YouTube, 2 Reddit, 1 TikTok = 5 total)
        samples = []
        samples.extend(select_youtube_samples(youtube_data, max_samples=2))
        samples.extend(select_reddit_samples(reddit_data, max_samples=2))
        samples.extend(select_tiktok_samples(all_tiktok_data, config['tiktok_metric'], max_samples=1))

        print(f"  Selected {len(samples)} samples")

        # Update content
        content = update_metric_samples(content, metric_name, samples)

    # Write updated file
    with open(METRIC_DATA_FILE, 'w', encoding='utf-8') as f:
        f.write(content)

    print("\n" + "=" * 80)
    print("COMPLETE")
    print(f"Updated: {METRIC_DATA_FILE}")
    print("=" * 80)


if __name__ == '__main__':
    main()
