#!/usr/bin/env python3
"""
TikTok data collector for the Absurdity Index.
Uses multiple strategies to collect TikTok content:
1. ProxiTok (privacy-friendly TikTok frontend) for hashtag discovery
2. TikTok's public oEmbed API for metadata enrichment
3. Fallback web scraping with respectful delays

No API key required.

Usage:
    python tiktok-collector.py
"""

import os
import re
import json
import time
import csv
import random
from datetime import datetime
from urllib.request import urlopen, Request
from urllib.error import HTTPError, URLError
from urllib.parse import quote

# Change to the script's directory
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
os.chdir(SCRIPT_DIR)

# ProxiTok instances (public mirrors of TikTok)
PROXITOK_INSTANCES = [
    'https://proxitok.pabloferreiro.es',
    'https://proxitok.odyssey346.dev',
    'https://proxitok.pussthecat.org',
    'https://tok.habedieehre.net',
]

# Hashtags to search by metric
METRIC_HASHTAGS = {
    'healthcare': [
        'insurancedenied', 'healthcarenightmare', 'medicaldebt',
        'priorauthorization', 'healthcaresystem', 'insurancescam',
        'deniedclaim', 'americanhealthcare', 'healthcareworker'
    ],
    'ai_psychosis': [
        'replika', 'characterai', 'aiboyfriend', 'aigirlfriend',
        'chatgpt', 'aicompanion', 'airelationship', 'replicaai'
    ],
    'subscription_overload': [
        'subscriptionfatigue', 'cancelsubscriptions', 'streamingservices',
        'toomanysubscriptions', 'subscriptiontrap', 'streamingwars'
    ],
    'wage_stagnation': [
        'paychecktopaycheck', 'workingpoor', 'minimumwage',
        'sidehustle', 'cantafford', 'costoflivingcrisis', 'wages'
    ],
    'housing_despair': [
        'housingcrisis', 'cantaffordrent', 'rentcrisis',
        'firsttimehomebuyer', 'pricedout', 'neverownhome', 'gentrification'
    ],
    'dating_app_despair': [
        'datingapps', 'hingehinge', 'bumble', 'tinder',
        'datingishard', 'moderndating', 'datingappfatigue', 'ghosted'
    ],
    'layoff_watch': [
        'techlayoffs', 'layoffs2024', 'layoffs2025', 'laidoff',
        'jobsearch', 'unemployment', 'hiringfreeze', 'firedtiktok'
    ],
    'airline_chaos': [
        'flightcancelled', 'airlinenightmare', 'lostluggage',
        'airportchaos', 'flightdelayed', 'worstairline', 'airlinehorrorstory'
    ]
}

# Keywords for severity categorization
LEVEL_3_KEYWORDS = [
    'destroyed', 'ruined', 'nightmare', 'horror', 'worst', 'crisis',
    'cant afford', "can't afford", 'homeless', 'bankrupt', 'died',
    'suicidal', 'depressed', 'anxiety', 'panic', 'trauma', 'addicted'
]

LEVEL_2_KEYWORDS = [
    'struggle', 'frustrated', 'angry', 'unfair', 'ridiculous',
    'expensive', 'stress', 'worried', 'scared', 'difficult', 'hard'
]


def categorize_content(text):
    """Categorize content by severity level."""
    text_lower = text.lower()

    for keyword in LEVEL_3_KEYWORDS:
        if keyword in text_lower:
            return 'LEVEL_3_CRISIS'

    for keyword in LEVEL_2_KEYWORDS:
        if keyword in text_lower:
            return 'LEVEL_2_FRUSTRATED'

    return 'LEVEL_1_CASUAL'


def get_random_headers():
    """Return randomized headers to avoid detection."""
    user_agents = [
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Safari/605.1.15',
    ]
    return {
        'User-Agent': random.choice(user_agents),
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.9',
    }


def fetch_proxitok_hashtag(hashtag, instance=None):
    """Fetch videos from a ProxiTok hashtag page."""
    if instance is None:
        instance = random.choice(PROXITOK_INSTANCES)

    url = f"{instance}/tag/{hashtag}"
    videos = []

    try:
        req = Request(url, headers=get_random_headers())
        response = urlopen(req, timeout=30)
        html = response.read().decode('utf-8')

        # Extract video links from ProxiTok HTML
        # ProxiTok uses /t/ paths for individual videos
        video_pattern = r'href="(/[@\w]+/video/\d+)"'
        matches = re.findall(video_pattern, html)

        # Also try to extract descriptions/titles
        desc_pattern = r'<p class="description"[^>]*>([^<]+)</p>'
        descriptions = re.findall(desc_pattern, html)

        for i, match in enumerate(matches[:20]):  # Limit to 20 per hashtag
            video_id = match.split('/')[-1]
            tiktok_url = f"https://www.tiktok.com{match}"

            videos.append({
                'video_id': video_id,
                'url': tiktok_url,
                'description': descriptions[i] if i < len(descriptions) else '',
                'source': 'proxitok'
            })

        return videos

    except HTTPError as e:
        print(f"      HTTP Error {e.code} on {instance}")
        return []
    except URLError as e:
        print(f"      URL Error: {e.reason}")
        return []
    except Exception as e:
        print(f"      Error: {e}")
        return []


def enrich_with_oembed(video_url):
    """Get metadata from TikTok's oEmbed API."""
    oembed_url = f"https://www.tiktok.com/oembed?url={quote(video_url, safe='')}"

    try:
        req = Request(oembed_url, headers=get_random_headers())
        response = urlopen(req, timeout=15)
        data = json.loads(response.read().decode('utf-8'))

        return {
            'title': data.get('title', ''),
            'author': data.get('author_name', ''),
            'author_url': data.get('author_url', ''),
            'thumbnail': data.get('thumbnail_url', ''),
        }
    except Exception as e:
        return None


def scrape_tiktok_hashtag_direct(hashtag):
    """
    Fallback: Try to scrape TikTok's hashtag page directly.
    This is less reliable but worth trying.
    """
    url = f"https://www.tiktok.com/tag/{hashtag}"
    videos = []

    try:
        req = Request(url, headers=get_random_headers())
        response = urlopen(req, timeout=30)
        html = response.read().decode('utf-8')

        # TikTok embeds video data in JSON within the page
        # Look for video IDs in the HTML
        video_id_pattern = r'"id":"(\d{19,})"'
        matches = re.findall(video_id_pattern, html)

        seen = set()
        for video_id in matches:
            if video_id not in seen:
                seen.add(video_id)
                videos.append({
                    'video_id': video_id,
                    'url': f"https://www.tiktok.com/video/{video_id}",
                    'description': '',
                    'source': 'tiktok_direct'
                })

        return videos[:15]  # Limit results

    except Exception as e:
        return []


def collect_metric_videos(metric_name, hashtags):
    """Collect videos for a single metric across all its hashtags."""
    print(f"\n{'='*60}")
    print(f"Collecting: {metric_name.upper().replace('_', ' ')}")
    print(f"{'='*60}")

    all_videos = []
    seen_ids = set()

    for hashtag in hashtags:
        print(f"\n  #{hashtag}...")

        # Try ProxiTok first (more reliable)
        videos = fetch_proxitok_hashtag(hashtag)

        # If ProxiTok fails, try direct scraping
        if not videos:
            print(f"    ProxiTok failed, trying direct...")
            videos = scrape_tiktok_hashtag_direct(hashtag)

        new_count = 0
        for video in videos:
            if video['video_id'] not in seen_ids:
                seen_ids.add(video['video_id'])
                video['hashtag'] = hashtag
                video['metric'] = metric_name
                all_videos.append(video)
                new_count += 1

        print(f"    Found {new_count} new videos")

        # Respectful delay between hashtags
        time.sleep(random.uniform(2, 4))

    return all_videos


def enrich_videos(videos, sample_size=50):
    """Enrich a sample of videos with oEmbed metadata."""
    print(f"\n  Enriching {min(sample_size, len(videos))} videos with oEmbed...")

    # Take a random sample if we have too many
    if len(videos) > sample_size:
        sample = random.sample(videos, sample_size)
    else:
        sample = videos

    enriched = []
    for i, video in enumerate(sample):
        oembed_data = enrich_with_oembed(video['url'])

        if oembed_data:
            video.update(oembed_data)
            # Use title for categorization
            text = f"{video.get('title', '')} {video.get('description', '')}"
            video['category'] = categorize_content(text)
            enriched.append(video)
            print(f"    [{i+1}/{len(sample)}] {video.get('author', 'unknown')}: {video.get('title', '')[:50]}...")

        # Rate limit oEmbed calls
        time.sleep(random.uniform(0.5, 1.5))

    return enriched


def main():
    print("=" * 80)
    print("TIKTOK DATA COLLECTION (Multi-Strategy)")
    print(f"Started: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 80)
    print("\nStrategies: ProxiTok scraping -> Direct fallback -> oEmbed enrichment")

    all_results = []

    for metric_name, hashtags in METRIC_HASHTAGS.items():
        videos = collect_metric_videos(metric_name, hashtags)

        if videos:
            # Enrich with oEmbed data
            enriched = enrich_videos(videos)
            all_results.extend(enriched)

            # Stats for this metric
            l3 = sum(1 for v in enriched if v.get('category') == 'LEVEL_3_CRISIS')
            l2 = sum(1 for v in enriched if v.get('category') == 'LEVEL_2_FRUSTRATED')
            l1 = sum(1 for v in enriched if v.get('category') == 'LEVEL_1_CASUAL')
            print(f"\n  {metric_name}: {len(enriched)} enriched | L1: {l1}, L2: {l2}, L3: {l3}")

        # Longer pause between metrics
        print("\n  Pausing between metrics...")
        time.sleep(random.uniform(5, 10))

    # Save results
    if all_results:
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        output_file = f'collected-data/tiktok_all_metrics_{timestamp}.csv'

        # Prepare data for CSV
        fieldnames = ['metric', 'hashtag', 'video_id', 'url', 'title', 'author',
                      'author_url', 'category', 'source', 'collected_date']

        rows = []
        for v in all_results:
            rows.append({
                'metric': v.get('metric', ''),
                'hashtag': v.get('hashtag', ''),
                'video_id': v.get('video_id', ''),
                'url': v.get('url', ''),
                'title': v.get('title', '')[:200],
                'author': v.get('author', ''),
                'author_url': v.get('author_url', ''),
                'category': v.get('category', 'LEVEL_1_CASUAL'),
                'source': v.get('source', ''),
                'collected_date': datetime.now().strftime('%Y-%m-%d')
            })

        with open(output_file, 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(rows)

        print(f"\n{'='*80}")
        print("COLLECTION COMPLETE")
        print(f"{'='*80}")
        print(f"Total videos collected: {len(all_results)}")
        print(f"Saved to: {output_file}")

        # Summary by metric
        print(f"\n{'='*80}")
        print("BY METRIC")
        print(f"{'='*80}")
        for metric in METRIC_HASHTAGS.keys():
            count = sum(1 for r in all_results if r.get('metric') == metric)
            print(f"  {metric.replace('_', ' ').title():25} {count:4} videos")
    else:
        print("\nNo videos collected. ProxiTok instances may be down.")
        print("Try again later or check instance availability.")


if __name__ == '__main__':
    main()
