#!/usr/bin/env python3
"""
Fetch view counts for Airline Chaos videos
"""

import csv
import requests
import os
from dotenv import load_dotenv

load_dotenv()
YOUTUBE_API_KEY = os.getenv('YOUTUBE_API_KEY')

def fetch_view_counts(video_ids):
    """Fetch view counts from YouTube API in batches of 50"""
    results = {}

    for i in range(0, len(video_ids), 50):
        batch = video_ids[i:i+50]
        video_id_string = ','.join(batch)

        url = f"https://www.googleapis.com/youtube/v3/videos?part=statistics&id={video_id_string}&key={YOUTUBE_API_KEY}"

        response = requests.get(url)
        data = response.json()

        for item in data.get('items', []):
            vid_id = item['id']
            stats = item.get('statistics', {})
            results[vid_id] = {
                'view_count': int(stats.get('viewCount', 0)),
                'comment_count': int(stats.get('commentCount', 0))
            }

    return results

# Read original CSV
input_file = 'collected-data/airline_chaos_youtube_20251220_021715.csv'
output_file = 'collected-data/airline_chaos_with_stats.csv'

videos = []
video_ids = []

with open(input_file, 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        videos.append(row)
        video_ids.append(row['video_id'])

print(f"Fetching stats for {len(video_ids)} videos...")

# Fetch view counts
stats = fetch_view_counts(video_ids)

# Add stats to videos
for video in videos:
    vid_id = video['video_id']
    if vid_id in stats:
        video['view_count'] = stats[vid_id]['view_count']
        video['comment_count'] = stats[vid_id]['comment_count']
    else:
        video['view_count'] = 0
        video['comment_count'] = 0

# Write new CSV
fieldnames = ['search_term', 'video_id', 'url', 'title', 'category', 'view_count', 'comment_count']
with open(output_file, 'w', newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(videos)

print(f"✓ Written {len(videos)} videos with stats to {output_file}")

# Show sample
print("\nSample videos:")
for video in videos[:3]:
    print(f"  {video['title'][:60]}... → {video['view_count']:,} views")
