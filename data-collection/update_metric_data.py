#!/usr/bin/env python3
"""
Automatically updates metricDetailData.ts with calculated scores from collected data.
This script is designed to run as part of the weekly automation pipeline.

Usage:
    python update_metric_data.py
"""

import csv
import json
import math
import os
import re
import glob
from datetime import datetime

# Change to the script's directory
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
os.chdir(SCRIPT_DIR)

METRIC_DATA_FILE = '../lib/metricDetailData.ts'

# Load centralized config
with open('config.json', 'r') as f:
    CONFIG = json.load(f)

# Build METRICS dict keyed by name (for regex matching in TS file)
METRICS = {}
for m in CONFIG['metrics']:
    METRICS[m['name']] = {
        'slug': m['slug'],
        'youtube_pattern': m['youtube_pattern'],
        'reddit_pattern': m['reddit_pattern'],
        'official_score': m['official_score']
    }

SEVERITY_WEIGHTS = CONFIG['severity_weights']
OFFICIAL_WEIGHT = CONFIG['formula']['official_weight']
SOCIAL_WEIGHT = CONFIG['formula']['social_weight']

# TikTok file pattern (contains all metrics)
TIKTOK_PATTERN = 'tiktok_youtube_*.csv'


def count_data_rows(filepath):
    """Count non-header rows in a CSV file."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            next(reader, None)  # skip header
            return sum(1 for _ in reader)
    except Exception:
        return 0


def get_latest_file(pattern, min_rows=5):
    """Get the most recent file matching the pattern that has real data.

    Skips files with fewer than min_rows data rows (likely failed collections).
    """
    files = glob.glob(f'collected-data/{pattern}')
    if not files:
        return None
    # Sort by filename descending (timestamps in filenames ensure chronological order)
    files.sort(reverse=True)
    for filepath in files:
        rows = count_data_rows(filepath)
        if rows >= min_rows:
            return filepath
    return None


def get_tiktok_data_for_metric(metric_slug):
    """Extract TikTok data for a specific metric from the combined file."""
    tiktok_file = get_latest_file(TIKTOK_PATTERN)
    if not tiktok_file:
        return [], {'L1': 0, 'L2': 0, 'L3': 0}, 0

    rows = []
    level_counts = {'L1': 0, 'L2': 0, 'L3': 0}

    try:
        with open(tiktok_file, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                if row.get('metric', '') == metric_slug:
                    rows.append(row)
                    category = row.get('category', '')
                    if 'LEVEL_1' in category:
                        level_counts['L1'] += 1
                    elif 'LEVEL_2' in category:
                        level_counts['L2'] += 1
                    elif 'LEVEL_3' in category:
                        level_counts['L3'] += 1
    except Exception as e:
        print(f"  Error reading TikTok data: {e}")

    return rows, level_counts, len(rows)


def get_engagement_value(row):
    """Extract the best engagement value from a row across different source formats."""
    for field in ('view_count', 'views', 'score', 'points', 'like_count'):
        try:
            val = int(row.get(field, 0) or 0)
            if val > 0:
                return val
        except (ValueError, TypeError):
            continue
    return 1


def get_source_data(pattern):
    """Read rows, level counts, and total from the latest file matching pattern."""
    csv_file = get_latest_file(pattern)
    if not csv_file:
        return [], {'L1': 0, 'L2': 0, 'L3': 0}, 0

    rows = []
    level_counts = {'L1': 0, 'L2': 0, 'L3': 0}

    try:
        with open(csv_file, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                rows.append(row)
                category = row.get('category', '')
                if 'LEVEL_1' in category:
                    level_counts['L1'] += 1
                elif 'LEVEL_2' in category:
                    level_counts['L2'] += 1
                elif 'LEVEL_3' in category:
                    level_counts['L3'] += 1
    except Exception as e:
        print(f"  Error reading {csv_file}: {e}")

    return rows, level_counts, len(rows)


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


def calculate_metric_scores():
    """Calculate scores for all metrics."""
    results = {}
    fred_scores = load_fred_scores()
    if fred_scores:
        print(f"FRED official scores loaded for: {', '.join(fred_scores.keys())}")

    for metric_name, config in METRICS.items():
        print(f"\nProcessing: {metric_name}")
        slug = config['slug']

        # Collect data from all sources
        sources = {}
        sources['youtube'] = get_source_data(config['youtube_pattern'])
        sources['reddit'] = get_source_data(config['reddit_pattern'])
        sources['tiktok'] = get_tiktok_data_for_metric(slug)
        sources['hackernews'] = get_source_data(f'{slug}_hackernews_*.csv')
        sources['cfpb'] = get_source_data(f'{slug}_cfpb_*.csv')
        sources['bluesky'] = get_source_data(f'{slug}_bluesky_*.csv')

        # Combine all rows for engagement-weighted scoring
        total_weighted = 0
        total_engagement = 0

        for source_name, (rows, levels, count) in sources.items():
            for row in rows:
                engagement_val = get_engagement_value(row)
                category = row.get('category', '')
                severity = SEVERITY_WEIGHTS.get(category, 0.33)
                engagement = math.log10(engagement_val + 1)
                total_weighted += severity * engagement
                total_engagement += engagement

        if total_engagement > 0:
            combined_social = (total_weighted / total_engagement) * 100
        else:
            combined_social = 0

        # Use FRED official score when available
        official = fred_scores.get(slug, config['official_score'])
        if slug in fred_scores:
            print(f"  Official: {official:.2f} (FRED)")
        final_score = (official * OFFICIAL_WEIGHT) + (combined_social * SOCIAL_WEIGHT)

        # Aggregate level counts and totals
        total_l1 = sum(s[1]['L1'] for s in sources.values())
        total_l2 = sum(s[1]['L2'] for s in sources.values())
        total_l3 = sum(s[1]['L3'] for s in sources.values())
        total_entries = sum(s[2] for s in sources.values())

        results[metric_name] = {
            'score': round(final_score, 2),
            'crisisRatio': round(combined_social, 2),
            'level1': total_l1,
            'level2': total_l2,
            'level3': total_l3,
            'total': total_entries,
            'youtube_count': sources['youtube'][2],
            'reddit_count': sources['reddit'][2],
            'tiktok_count': sources['tiktok'][2],
            'hackernews_count': sources['hackernews'][2],
            'cfpb_count': sources['cfpb'][2],
            'bluesky_count': sources['bluesky'][2],
        }

        counts = [f"YT:{sources['youtube'][2]}", f"RD:{sources['reddit'][2]}",
                  f"TT:{sources['tiktok'][2]}", f"HN:{sources['hackernews'][2]}",
                  f"CFPB:{sources['cfpb'][2]}", f"BS:{sources['bluesky'][2]}"]
        print(f"  {', '.join(counts)}, Total: {total_entries}")
        print(f"  Score: {final_score:.2f}, Crisis Ratio: {combined_social:.2f}")

    return results


def read_current_scores():
    """Read current scores from the TypeScript file before overwriting."""
    scores = {}
    try:
        with open(METRIC_DATA_FILE, 'r', encoding='utf-8') as f:
            content = f.read()
        for metric_name in METRICS:
            pattern = rf'title: "{re.escape(metric_name)}",\s*score: ([\d.]+)'
            match = re.search(pattern, content)
            if match:
                scores[metric_name] = float(match.group(1))
    except Exception as e:
        print(f"  Could not read previous scores: {e}")
    return scores


def calculate_trend(old_score, new_score, threshold=2.0):
    """Determine trend based on score change.

    A threshold prevents noise from flipping the trend on tiny fluctuations.
    """
    if old_score is None:
        return 'worsening'  # default for first run
    diff = new_score - old_score
    if diff > threshold:
        return 'worsening'
    elif diff < -threshold:
        return 'improving'
    return 'neutral'


def update_typescript_file(results):
    """Update the metricDetailData.ts file with new scores."""
    previous_scores = read_current_scores()

    with open(METRIC_DATA_FILE, 'r', encoding='utf-8') as f:
        content = f.read()

    today = datetime.now().strftime('%B %d, %Y').replace(' 0', ' ')

    for metric_name, data in results.items():
        print(f"\nUpdating {metric_name}...")

        # Update score
        pattern = rf'("{re.escape(metric_name)}": \{{\s*title: "{re.escape(metric_name)}",\s*score: )[\d.]+'
        replacement = rf'\g<1>{data["score"]}'
        content = re.sub(pattern, replacement, content)

        # Update crisisRatio
        pattern = rf'(title: "{re.escape(metric_name)}",\s*score: [\d.]+,\s*label: "[^"]+",\s*trend: "[^"]+",\s*officialScore: [\d.]+,\s*crisisRatio: )[\d.]+'
        replacement = rf'\g<1>{data["crisisRatio"]}'
        content = re.sub(pattern, replacement, content)

        # Update trend
        old_score = previous_scores.get(metric_name)
        trend = calculate_trend(old_score, data['score'])
        data['trend'] = trend
        pattern = rf'(title: "{re.escape(metric_name)}",\s*score: [\d.]+,\s*label: "[^"]+",\s*trend: )"[^"]+"'
        replacement = rf'\g<1>"{trend}"'
        content = re.sub(pattern, replacement, content)
        if old_score is not None:
            print(f"  Trend: {old_score:.2f} -> {data['score']:.2f} = {trend}")
        else:
            print(f"  Trend: no previous score, defaulting to {trend}")

        # Update levelDistribution
        pattern = rf'(title: "{re.escape(metric_name)}".*?levelDistribution: \{{\s*level1: )\d+'
        replacement = rf'\g<1>{data["level1"]}'
        content = re.sub(pattern, replacement, content, flags=re.DOTALL)

        pattern = rf'(title: "{re.escape(metric_name)}".*?levelDistribution: \{{[^}}]*level2: )\d+'
        replacement = rf'\g<1>{data["level2"]}'
        content = re.sub(pattern, replacement, content, flags=re.DOTALL)

        pattern = rf'(title: "{re.escape(metric_name)}".*?levelDistribution: \{{[^}}]*level3: )\d+'
        replacement = rf'\g<1>{data["level3"]}'
        content = re.sub(pattern, replacement, content, flags=re.DOTALL)

        pattern = rf'(title: "{re.escape(metric_name)}".*?levelDistribution: \{{[^}}]*total: )\d+'
        replacement = rf'\g<1>{data["total"]}'
        content = re.sub(pattern, replacement, content, flags=re.DOTALL)

        # Update lastUpdated
        pattern = rf'(title: "{re.escape(metric_name)}".*?lastUpdated: ")[^"]+'
        replacement = rf'\g<1>{today}'
        content = re.sub(pattern, replacement, content, flags=re.DOTALL)

        # Update collectionProgress counts and percentages for YouTube
        if data.get('youtube_count', 0) > 0:
            pattern = rf'(title: "{re.escape(metric_name)}".*?platform: "YouTube",\s*current: )\d+'
            replacement = rf'\g<1>{data["youtube_count"]}'
            content = re.sub(pattern, replacement, content, flags=re.DOTALL)

        # Update collectionProgress counts and percentages for Reddit
        if data.get('reddit_count', 0) > 0:
            pattern = rf'(title: "{re.escape(metric_name)}".*?platform: "Reddit",\s*current: )\d+'
            replacement = rf'\g<1>{data["reddit_count"]}'
            content = re.sub(pattern, replacement, content, flags=re.DOTALL)

        # Update collectionProgress counts and percentages for TikTok
        tiktok_count = data.get('tiktok_count', 0)
        if tiktok_count > 0:
            pattern = rf'(title: "{re.escape(metric_name)}".*?platform: "TikTok",\s*current: )\d+'
            replacement = rf'\g<1>{tiktok_count}'
            content = re.sub(pattern, replacement, content, flags=re.DOTALL)
            # Also update the percentage (assuming target of 100-120)
            pattern = rf'(title: "{re.escape(metric_name)}".*?platform: "TikTok",\s*current: \d+,\s*target: )(\d+)(,\s*percentage: )\d+'
            def calc_percentage(match):
                target = int(match.group(2))
                pct = min(100, int(tiktok_count / target * 100))
                return f'{match.group(1)}{target}{match.group(3)}{pct}'
            content = re.sub(pattern, calc_percentage, content, flags=re.DOTALL)

        # Update dataSources counts (e.g., "YouTube: 170 videos" -> "YouTube: 135 videos")
        if data.get('youtube_count', 0) > 0:
            pattern = rf'(title: "{re.escape(metric_name)}".*?dataSources:.*?"YouTube: )\d+( videos)'
            replacement = rf'\g<1>{data["youtube_count"]}\g<2>'
            content = re.sub(pattern, replacement, content, flags=re.DOTALL)

        if data.get('reddit_count', 0) > 0:
            pattern = rf'(title: "{re.escape(metric_name)}".*?dataSources:.*?"Reddit: )\d+( posts)'
            replacement = rf'\g<1>{data["reddit_count"]}\g<2>'
            content = re.sub(pattern, replacement, content, flags=re.DOTALL)

        if data.get('tiktok_count', 0) > 0:
            pattern = rf'(title: "{re.escape(metric_name)}".*?dataSources:.*?"TikTok: )\d+( videos)'
            replacement = rf'\g<1>{data["tiktok_count"]}\g<2>'
            content = re.sub(pattern, replacement, content, flags=re.DOTALL)

        if data.get('hackernews_count', 0) > 0:
            pattern = rf'(title: "{re.escape(metric_name)}".*?dataSources:.*?"Hacker News: )\d+( stories)'
            replacement = rf'\g<1>{data["hackernews_count"]}\g<2>'
            content = re.sub(pattern, replacement, content, flags=re.DOTALL)

        if data.get('cfpb_count', 0) > 0:
            pattern = rf'(title: "{re.escape(metric_name)}".*?dataSources:.*?"CFPB: )\d+( complaints)'
            replacement = rf'\g<1>{data["cfpb_count"]}\g<2>'
            content = re.sub(pattern, replacement, content, flags=re.DOTALL)

        if data.get('bluesky_count', 0) > 0:
            pattern = rf'(title: "{re.escape(metric_name)}".*?dataSources:.*?"Bluesky: )\d+( posts)'
            replacement = rf'\g<1>{data["bluesky_count"]}\g<2>'
            content = re.sub(pattern, replacement, content, flags=re.DOTALL)

    with open(METRIC_DATA_FILE, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"\nUpdated {METRIC_DATA_FILE}")


def main():
    print("=" * 80)
    print("ABSURDITY INDEX - AUTOMATED METRIC DATA UPDATE")
    print(f"Started: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 80)

    results = calculate_metric_scores()

    print("\n" + "=" * 80)
    print("SUMMARY")
    print("=" * 80)
    for name, data in results.items():
        print(f"{name:25} -> Score: {data['score']:5.2f}, Entries: {data['total']}")

    print("\n" + "=" * 80)
    print("UPDATING TYPESCRIPT FILE")
    print("=" * 80)
    update_typescript_file(results)

    print("\n" + "=" * 80)
    print("COMPLETE")
    print("=" * 80)


if __name__ == '__main__':
    main()
