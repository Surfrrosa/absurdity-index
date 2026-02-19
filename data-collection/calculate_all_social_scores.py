#!/usr/bin/env python3
"""
Calculate social scores for all metrics using the latest available data.
Auto-detects the most recent CSV files for each source.

Usage:
    python calculate_all_social_scores.py
"""

import csv
import glob
import json
import math
import os
from datetime import datetime

# Change to script directory
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
os.chdir(SCRIPT_DIR)

# Load centralized config
with open('config.json', 'r') as f:
    CONFIG = json.load(f)

METRICS = CONFIG['metrics']
SEVERITY_WEIGHTS = CONFIG['severity_weights']
OFFICIAL_WEIGHT = CONFIG['formula']['official_weight']
SOCIAL_WEIGHT = CONFIG['formula']['social_weight']


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

    # Hacker News data
    hn_file = find_latest_file(f'collected-data/{slug}_hackernews_*.csv')
    if hn_file:
        files.append(hn_file)
        sources_found.append('Hacker News')

    # CFPB complaint data
    cfpb_file = find_latest_file(f'collected-data/{slug}_cfpb_*.csv')
    if cfpb_file:
        files.append(cfpb_file)
        sources_found.append('CFPB')

    # Bluesky data
    bluesky_file = find_latest_file(f'collected-data/{slug}_bluesky_*.csv')
    if bluesky_file:
        files.append(bluesky_file)
        sources_found.append('Bluesky')

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

        # Get engagement value (views for YouTube/TikTok, score for Reddit,
        # points for HN, like_count for Bluesky)
        view_count = 0
        for field in ['view_count', 'views', 'score', 'points', 'like_count']:
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


def load_fred_scores():
    """Load FRED official scores if the file exists."""
    fred_file = 'collected-data/official_scores.json'
    if not os.path.exists(fred_file):
        return {}
    try:
        with open(fred_file, 'r') as f:
            data = json.load(f)
        scores = {}
        for slug, info in data.get('scores', {}).items():
            if info.get('source') == 'fred':
                scores[slug] = info['score']
        return scores
    except Exception as e:
        print(f"  Warning: Could not load FRED scores: {e}")
        return {}


def calculate_metric_score(metric, fred_scores=None):
    """Calculate the full score for a metric using all available data sources."""
    slug = metric['slug']
    name = metric['name']

    print(f"\n{name}:")
    print("-" * 40)

    all_rows = []

    # Find YouTube, Reddit, HN, CFPB, and Bluesky files
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

    # Use FRED official score when available, otherwise config fallback
    official_score = metric['official_score']
    if fred_scores and slug in fred_scores:
        official_score = fred_scores[slug]
        print(f"  Official Score: {official_score:.2f} (from FRED)")
    else:
        print(f"  Official Score: {official_score:.2f} (from config)")

    final_score = (official_score * OFFICIAL_WEIGHT) + (social_score * SOCIAL_WEIGHT)

    total = len(all_rows)
    print(f"  Sources: {', '.join(sources)}")
    print(f"  Total entries: {total}")
    print(f"  Distribution: L1={levels['L1']}, L2={levels['L2']}, L3={levels['L3']}")
    print(f"  Social Score: {social_score:.2f}")
    print(f"  Final Score: {final_score:.2f}")

    return {
        'name': name,
        'slug': slug,
        'official': official_score,
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

    # Load FRED official scores (if available)
    fred_scores = load_fred_scores()
    if fred_scores:
        print(f"\nFRED official scores loaded for: {', '.join(fred_scores.keys())}")
    else:
        print("\nNo FRED official scores found, using config.json fallbacks.")

    results = []

    for metric in METRICS:
        result = calculate_metric_score(metric, fred_scores)
        if result:
            results.append(result)

    # Summary
    print("\n" + "=" * 80)
    print("SUMMARY FOR UPDATING metricDetailData.ts")
    print("=" * 80)
    print()

    total_entries = sum(r['total'] for r in results)

    for r in results:
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

    fred_file = 'collected-data/official_scores.json'
    if os.path.exists(fred_file):
        print(f"\nFRED official scores:")
        print(f"  official_scores.json")


if __name__ == '__main__':
    main()
