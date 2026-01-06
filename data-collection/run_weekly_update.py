#!/usr/bin/env python3
"""
Master script for running all data collectors for the Absurdity Index.
Run this script to perform a complete weekly data collection update.

Usage:
    python run_weekly_update.py
    python run_weekly_update.py --youtube-only
    python run_weekly_update.py --reddit-only
"""

import subprocess
import sys
import time
import os
from datetime import datetime

# Change to the script's directory
os.chdir(os.path.dirname(os.path.abspath(__file__)))

YOUTUBE_COLLECTORS = [
    'healthcare-youtube-collector.py',
    'ai-psychosis-youtube-collector.py',
    'subscription-overload-youtube-collector.py',
    'wage-stagnation-youtube-collector.py',
    'housing-despair-youtube-collector.py',
    'dating-app-despair-youtube-collector.py',
    'layoff-watch-youtube-collector.py',
    'airline-chaos-youtube-collector.py',
]

REDDIT_COLLECTORS = [
    'healthcare-reddit-collector.py',
    'ai-psychosis-reddit-collector.py',
    'subscription-overload-reddit-collector.py',
    'wage-stagnation-reddit-collector.py',
    'housing-despair-reddit-collector.py',
    'dating-app-despair-reddit-collector.py',
    'layoff-watch-reddit-collector.py',
    'airline-chaos-reddit-collector.py',
]

def run_collector(script_name, delay_after=0):
    """Run a single collector script."""
    print(f"\n{'='*60}")
    print(f"Running: {script_name}")
    print(f"{'='*60}")

    try:
        result = subprocess.run(
            [sys.executable, script_name],
            capture_output=False,
            text=True,
            timeout=300  # 5 minute timeout per script
        )
        if result.returncode == 0:
            print(f"SUCCESS: {script_name}")
        else:
            print(f"WARNING: {script_name} returned code {result.returncode}")
    except subprocess.TimeoutExpired:
        print(f"TIMEOUT: {script_name} took too long")
    except Exception as e:
        print(f"ERROR: {script_name} failed with {e}")

    if delay_after > 0:
        print(f"Waiting {delay_after} seconds before next collector...")
        time.sleep(delay_after)

def run_all_youtube():
    """Run all YouTube collectors."""
    print("\n" + "="*80)
    print("RUNNING YOUTUBE COLLECTORS")
    print("="*80)

    for script in YOUTUBE_COLLECTORS:
        run_collector(script, delay_after=5)

def run_all_reddit():
    """Run all Reddit collectors with delays to avoid rate limiting."""
    print("\n" + "="*80)
    print("RUNNING REDDIT COLLECTORS (with rate limit delays)")
    print("="*80)

    for script in REDDIT_COLLECTORS:
        run_collector(script, delay_after=20)  # 20 second delay between Reddit calls

def calculate_scores():
    """Run the score calculator."""
    print("\n" + "="*80)
    print("CALCULATING SOCIAL SCORES")
    print("="*80)

    run_collector('calculate_all_social_scores.py')

def update_typescript():
    """Update the metricDetailData.ts file."""
    print("\n" + "="*80)
    print("UPDATING metricDetailData.ts")
    print("="*80)

    run_collector('update_metric_data.py')

def main():
    start_time = datetime.now()
    print(f"\n{'#'*80}")
    print(f"ABSURDITY INDEX - WEEKLY DATA UPDATE")
    print(f"Started: {start_time.strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"{'#'*80}")

    youtube_only = '--youtube-only' in sys.argv
    reddit_only = '--reddit-only' in sys.argv
    no_update = '--no-update' in sys.argv

    if youtube_only:
        run_all_youtube()
    elif reddit_only:
        run_all_reddit()
    else:
        run_all_youtube()
        run_all_reddit()

    calculate_scores()

    if not no_update:
        update_typescript()

    end_time = datetime.now()
    duration = end_time - start_time

    print(f"\n{'#'*80}")
    print(f"DATA COLLECTION COMPLETE")
    print(f"Duration: {duration}")
    print(f"Finished: {end_time.strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"{'#'*80}")
    print("\nNext step: Commit and push the changes to trigger a Vercel deployment.")
    print("  git add -A && git commit -m 'Weekly data update' && git push")

if __name__ == '__main__':
    main()
