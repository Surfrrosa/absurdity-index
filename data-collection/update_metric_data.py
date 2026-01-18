#!/usr/bin/env python3
"""
Automatically updates metricDetailData.ts with calculated scores from collected data.
This script is designed to run as part of the weekly automation pipeline.

Usage:
    python update_metric_data.py
"""

import csv
import math
import os
import re
import glob
from datetime import datetime

# Change to the script's directory
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
os.chdir(SCRIPT_DIR)

METRIC_DATA_FILE = '../lib/metricDetailData.ts'

# Metric configurations with official scores
METRICS = {
    'What Healthcare?': {
        'slug': 'healthcare',
        'youtube_pattern': 'healthcare_youtube_*.csv',
        'reddit_pattern': 'healthcare_reddit_*.csv',
        'official_score': 56.30
    },
    'AI Psychosis': {
        'slug': 'ai_psychosis',
        'youtube_pattern': 'ai_psychosis_youtube_*.csv',
        'reddit_pattern': 'ai_psychosis_reddit_*.csv',
        'official_score': 12.5
    },
    'Subscription Overload': {
        'slug': 'subscription_overload',
        'youtube_pattern': 'subscription_overload_youtube_*.csv',
        'reddit_pattern': 'subscription_overload_reddit_*.csv',
        'official_score': 45.2
    },
    'Wage Stagnation': {
        'slug': 'wage_stagnation',
        'youtube_pattern': 'wage_stagnation_youtube_*.csv',
        'reddit_pattern': 'wage_stagnation_reddit_*.csv',
        'official_score': 38.4
    },
    'Housing Despair': {
        'slug': 'housing_despair',
        'youtube_pattern': 'housing_despair_youtube_*.csv',
        'reddit_pattern': 'housing_despair_reddit_*.csv',
        'official_score': 37.6
    },
    'Dating App Despair': {
        'slug': 'dating_app_despair',
        'youtube_pattern': 'dating_app_despair_youtube_*.csv',
        'reddit_pattern': 'dating_app_despair_reddit_*.csv',
        'official_score': 8.5
    },
    'Layoff Watch': {
        'slug': 'layoff_watch',
        'youtube_pattern': 'layoff_watch_youtube_*.csv',
        'reddit_pattern': 'layoff_watch_reddit_*.csv',
        'official_score': 76.5
    },
    'Airline Chaos': {
        'slug': 'airline_chaos',
        'youtube_pattern': 'airline_chaos_youtube_*.csv',
        'reddit_pattern': 'airline_chaos_reddit_*.csv',
        'official_score': 21.0
    }
}

# TikTok file pattern (contains all metrics)
TIKTOK_PATTERN = 'tiktok_youtube_*.csv'

SEVERITY_WEIGHTS = {
    'LEVEL_1_AWARE': 0.33,
    'LEVEL_1_CASUAL': 0.33,
    'LEVEL_2_STRUGGLING': 0.67,
    'LEVEL_2_FRUSTRATED': 0.67,
    'LEVEL_2_DEPENDENT': 0.67,
    'LEVEL_3_CRISIS': 1.0
}


def get_latest_file(pattern):
    """Get the most recent file matching the pattern."""
    files = glob.glob(f'collected-data/{pattern}')
    if not files:
        return None
    return max(files, key=os.path.getmtime)


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


def calculate_score_from_csv(csv_file):
    """Calculate engagement-weighted severity score from a CSV file."""
    if not csv_file or not os.path.exists(csv_file):
        return None, None, 0

    total_weighted_score = 0
    total_engagement = 0
    level_counts = {'L1': 0, 'L2': 0, 'L3': 0}
    total_entries = 0

    try:
        with open(csv_file, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                total_entries += 1
                category = row.get('category', '')

                view_count = int(row.get('view_count', 0) or 0)
                score = int(row.get('score', 0) or 0)
                engagement_value = max(view_count, score, 1)

                if 'LEVEL_1' in category:
                    level_counts['L1'] += 1
                elif 'LEVEL_2' in category:
                    level_counts['L2'] += 1
                elif 'LEVEL_3' in category:
                    level_counts['L3'] += 1

                severity = SEVERITY_WEIGHTS.get(category, 0.33)
                engagement = math.log10(engagement_value + 1)
                total_weighted_score += severity * engagement
                total_engagement += engagement

    except Exception as e:
        print(f"  Error processing {csv_file}: {e}")
        return None, None, 0

    if total_engagement == 0:
        return 0, level_counts, total_entries

    social_score = (total_weighted_score / total_engagement) * 100
    return social_score, level_counts, total_entries


def calculate_metric_scores():
    """Calculate scores for all metrics."""
    results = {}

    for metric_name, config in METRICS.items():
        print(f"\nProcessing: {metric_name}")

        youtube_file = get_latest_file(config['youtube_pattern'])
        reddit_file = get_latest_file(config['reddit_pattern'])

        youtube_score, youtube_levels, youtube_count = calculate_score_from_csv(youtube_file)
        reddit_score, reddit_levels, reddit_count = calculate_score_from_csv(reddit_file)

        # Get TikTok data for this metric
        tiktok_rows, tiktok_levels, tiktok_count = get_tiktok_data_for_metric(config['slug'])

        # Combine scores
        total_weighted = 0
        total_engagement = 0

        if youtube_file and os.path.exists(youtube_file):
            with open(youtube_file, 'r', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    view_count = int(row.get('view_count', 0) or 0)
                    category = row.get('category', '')
                    severity = SEVERITY_WEIGHTS.get(category, 0.33)
                    engagement = math.log10(max(view_count, 1) + 1)
                    total_weighted += severity * engagement
                    total_engagement += engagement

        if reddit_file and os.path.exists(reddit_file):
            with open(reddit_file, 'r', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    score = int(row.get('score', 0) or 0)
                    category = row.get('category', '')
                    severity = SEVERITY_WEIGHTS.get(category, 0.33)
                    engagement = math.log10(max(score, 1) + 1)
                    total_weighted += severity * engagement
                    total_engagement += engagement

        # Add TikTok data
        for row in tiktok_rows:
            views = int(row.get('views', 0) or 0)
            category = row.get('category', '')
            severity = SEVERITY_WEIGHTS.get(category, 0.33)
            engagement = math.log10(max(views, 1) + 1)
            total_weighted += severity * engagement
            total_engagement += engagement

        if total_engagement > 0:
            combined_social = (total_weighted / total_engagement) * 100
        else:
            combined_social = 0

        # Calculate final score
        official = config['official_score']
        final_score = (official * 0.4) + (combined_social * 0.6)

        # Combine level counts
        total_l1 = (youtube_levels['L1'] if youtube_levels else 0) + (reddit_levels['L1'] if reddit_levels else 0) + tiktok_levels['L1']
        total_l2 = (youtube_levels['L2'] if youtube_levels else 0) + (reddit_levels['L2'] if reddit_levels else 0) + tiktok_levels['L2']
        total_l3 = (youtube_levels['L3'] if youtube_levels else 0) + (reddit_levels['L3'] if reddit_levels else 0) + tiktok_levels['L3']
        total_entries = youtube_count + reddit_count + tiktok_count

        results[metric_name] = {
            'score': round(final_score, 2),
            'crisisRatio': round(combined_social, 2),
            'level1': total_l1,
            'level2': total_l2,
            'level3': total_l3,
            'total': total_entries,
            'youtube_count': youtube_count,
            'reddit_count': reddit_count,
            'tiktok_count': tiktok_count
        }

        print(f"  YouTube: {youtube_count}, Reddit: {reddit_count}, TikTok: {tiktok_count}, Total: {total_entries}")
        print(f"  Score: {final_score:.2f}, Crisis Ratio: {combined_social:.2f}")

    return results


def update_typescript_file(results):
    """Update the metricDetailData.ts file with new scores."""
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
