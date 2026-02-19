#!/usr/bin/env python3
"""
Calculate social scores for all metrics using the latest available data.
Auto-detects the most recent CSV files for each source.

Usage:
    python calculate_all_social_scores.py
"""

import csv
import glob
import math
import os
from datetime import datetime

# Change to script directory
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
os.chdir(SCRIPT_DIR)

# Metric configurations with file patterns (not hardcoded paths)
METRICS = [
    {
        'name': 'What Healthcare?',
        'slug': 'healthcare',
        'official_score': 56.30
    },
    {
        'name': 'AI Psychosis',
        'slug': 'ai_psychosis',
        'official_score': 12.5
    },
    {
        'name': 'Subscription Overload',
        'slug': 'subscription_overload',
        'official_score': 45.2
    },
    {
        'name': 'Wage Stagnation',
        'slug': 'wage_stagnation',
        'official_score': 38.4
    },
    {
        'name': 'Housing Despair',
        'slug': 'housing_despair',
        'official_score': 37.6
    },
    {
        'name': 'Dating App Despair',
        'slug': 'dating_app_despair',
        'official_score': 8.5
    },
    {
        'name': 'Layoff Watch',
        'slug': 'layoff_watch',
        'official_score': 76.5
    },
    {
        'name': 'Airline Chaos',
        'slug': 'airline_chaos',
        'official_score': 21.0
    }
]

# Severity weights for scoring
SEVERITY_WEIGHTS = {
    'LEVEL_1_AWARE': 0.33,
    'LEVEL_1_CASUAL': 0.33,
    'LEVEL_2_STRUGGLING': 0.67,
    'LEVEL_2_FRUSTRATED': 0.67,
    'LEVEL_2_DEPENDENT': 0.67,
    'LEVEL_3_CRISIS': 1.0
}


def count_data_rows(filepath):
    """Count non-header rows in a CSV file."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            next(reader, None)  # skip header
            return sum(1 for _ in reader)
    except Exception:
        return 0


def find_latest_file(pattern, min_rows=5):
    """Find the most recent file matching a glob pattern that has real data.

    Files are expected to have timestamps in format: *_YYYYMMDD_HHMMSS.csv
    Skips files with fewer than min_rows data rows (likely failed collections).
    Returns the path to the most recent file with data, or None if no matches.
    """
    matches = glob.glob(pattern)

    if not matches:
        return None

    # Sort by filename (timestamps in filename ensure chronological order)
    matches.sort(reverse=True)

    for filepath in matches:
        rows = count_data_rows(filepath)
        if rows >= min_rows:
            return filepath
        else:
            print(f"  Skipping {os.path.basename(filepath)} ({rows} rows, need >={min_rows})")

    return None


def find_metric_files(slug):
    """Find all latest data files for a metric across all sources."""
    files = []
    sources_found = []

    # YouTube data
    youtube_file = find_latest_file(f'collected-data/{slug}_youtube_*.csv')
    if youtube_file:
        files.append(youtube_file)
        sources_found.append('YouTube')

    # Reddit data
    reddit_file = find_latest_file(f'collected-data/{slug}_reddit_*.csv')
    if reddit_file:
        files.append(reddit_file)
        sources_found.append('Reddit')

    # TikTok data (collected via YouTube compilations)
    # TikTok files contain all metrics, so we'll handle them separately

    return files, sources_found


def find_tiktok_data(metric_slug):
    """Extract TikTok data for a specific metric from the combined file."""
    tiktok_file = find_latest_file('collected-data/tiktok_youtube_*.csv')

    if not tiktok_file:
        return []

    rows = []
    try:
        with open(tiktok_file, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                if row.get('metric', '') == metric_slug:
                    rows.append(row)
    except Exception as e:
        print(f"  Error reading TikTok data: {e}")

    return rows


def calculate_score_from_rows(rows):
    """Calculate engagement-weighted severity score from data rows."""
    total_weighted_score = 0
    total_engagement = 0
    level_counts = {'L1': 0, 'L2': 0, 'L3': 0}

    for row in rows:
        category = row.get('category', '')

        # Get engagement value (views for YouTube/TikTok, score for Reddit)
        view_count = 0
        for field in ['view_count', 'views', 'score']:
            try:
                view_count = int(row.get(field, 0) or 0)
                if view_count > 0:
                    break
            except (ValueError, TypeError):
                continue

        engagement_value = max(view_count, 1)

        # Count levels
        if 'LEVEL_1' in category:
            level_counts['L1'] += 1
        elif 'LEVEL_2' in category:
            level_counts['L2'] += 1
        elif 'LEVEL_3' in category:
            level_counts['L3'] += 1

        # Get severity weight
        severity = SEVERITY_WEIGHTS.get(category, 0.33)

        # Calculate engagement weight (logarithmic)
        engagement = math.log10(engagement_value + 1)

        # Add contribution
        total_weighted_score += severity * engagement
        total_engagement += engagement

    # Calculate final score (0-100 scale)
    if total_engagement == 0:
        return 0, level_counts

    social_score = (total_weighted_score / total_engagement) * 100
    return social_score, level_counts


def calculate_metric_score(metric):
    """Calculate the full score for a metric using all available data sources."""
    slug = metric['slug']
    name = metric['name']

    print(f"\n{name}:")
    print("-" * 40)

    all_rows = []

    # Find YouTube and Reddit files
    files, sources = find_metric_files(slug)

    for csv_file in files:
        try:
            with open(csv_file, 'r', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                rows = list(reader)
                all_rows.extend(rows)
                filename = os.path.basename(csv_file)
                print(f"  {filename}: {len(rows)} entries")
        except Exception as e:
            print(f"  Error reading {csv_file}: {e}")

    # Add TikTok data
    tiktok_rows = find_tiktok_data(slug)
    if tiktok_rows:
        all_rows.extend(tiktok_rows)
        print(f"  TikTok (via YouTube): {len(tiktok_rows)} entries")
        sources.append('TikTok')

    if not all_rows:
        print(f"  WARNING: No data found for {name}")
        return None

    # Calculate scores
    social_score, levels = calculate_score_from_rows(all_rows)
    final_score = (metric['official_score'] * 0.4) + (social_score * 0.6)

    total = len(all_rows)
    print(f"  Sources: {', '.join(sources)}")
    print(f"  Total entries: {total}")
    print(f"  Distribution: L1={levels['L1']}, L2={levels['L2']}, L3={levels['L3']}")
    print(f"  Official Score: {metric['official_score']:.2f}")
    print(f"  Social Score: {social_score:.2f}")
    print(f"  Final Score: {final_score:.2f}")

    return {
        'name': name,
        'slug': slug,
        'official': metric['official_score'],
        'social': social_score,
        'final': final_score,
        'total': total,
        'levels': levels,
        'sources': sources
    }


def main():
    print("=" * 80)
    print("CALCULATING ALL SOCIAL SCORES")
    print("Auto-detecting latest data files")
    print(f"Run time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 80)

    results = []

    for metric in METRICS:
        result = calculate_metric_score(metric)
        if result:
            results.append(result)

    # Summary
    print("\n" + "=" * 80)
    print("SUMMARY FOR UPDATING metricDetailData.ts")
    print("=" * 80)
    print()

    total_entries = sum(r['total'] for r in results)

    for r in results:
        crisis_pct = (r['levels']['L2'] + r['levels']['L3']) / r['total'] * 100 if r['total'] > 0 else 0
        print(f"{r['name']:25} score: {r['final']:5.2f}  |  social: {r['social']:5.2f}  |  entries: {r['total']:4}")

    print()
    print(f"Total data entries across all metrics: {total_entries}")

    # Show which files were used
    print("\n" + "=" * 80)
    print("DATA FILES USED")
    print("=" * 80)

    for metric in METRICS:
        files, _ = find_metric_files(metric['slug'])
        print(f"\n{metric['name']}:")
        for f in files:
            print(f"  {os.path.basename(f)}")

    tiktok_file = find_latest_file('collected-data/tiktok_youtube_*.csv')
    if tiktok_file:
        print(f"\nTikTok (all metrics):")
        print(f"  {os.path.basename(tiktok_file)}")


if __name__ == '__main__':
    main()
