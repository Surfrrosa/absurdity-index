#!/usr/bin/env python3
"""
Auto-update sampleData arrays in metricDetailData.ts from collected data.

This script:
1. Reads the latest collected data for each metric (YouTube, Reddit, TikTok, HN, CFPB)
2. Selects representative samples (mix of severity levels and platforms)
3. Strips emoji characters from sample content
4. Updates the sampleData arrays in metricDetailData.ts

Run this AFTER data collection, BEFORE or AFTER update_metric_data.py

Usage:
    python update_sample_data.py
"""

import os
import csv
import glob
import html
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
        'slug': 'healthcare',
        'youtube_pattern': 'healthcare_youtube_*.csv',
        'reddit_pattern': 'healthcare_reddit_*.csv',
        'tiktok_metric': 'healthcare'
    },
    'AI Psychosis': {
        'slug': 'ai_psychosis',
        'youtube_pattern': 'ai_psychosis_youtube_*.csv',
        'reddit_pattern': 'ai_psychosis_reddit_*.csv',
        'tiktok_metric': 'ai_psychosis'
    },
    'Subscription Overload': {
        'slug': 'subscription_overload',
        'youtube_pattern': 'subscription_overload_youtube_*.csv',
        'reddit_pattern': 'subscription_overload_reddit_*.csv',
        'tiktok_metric': 'subscription_overload'
    },
    'Wage Stagnation': {
        'slug': 'wage_stagnation',
        'youtube_pattern': 'wage_stagnation_youtube_*.csv',
        'reddit_pattern': 'wage_stagnation_reddit_*.csv',
        'tiktok_metric': 'wage_stagnation'
    },
    'Housing Despair': {
        'slug': 'housing_despair',
        'youtube_pattern': 'housing_despair_youtube_*.csv',
        'reddit_pattern': 'housing_despair_reddit_*.csv',
        'tiktok_metric': 'housing_despair'
    },
    'Dating App Despair': {
        'slug': 'dating_app_despair',
        'youtube_pattern': 'dating_app_despair_youtube_*.csv',
        'reddit_pattern': 'dating_app_despair_reddit_*.csv',
        'tiktok_metric': 'dating_app_despair'
    },
    'Layoff Watch': {
        'slug': 'layoff_watch',
        'youtube_pattern': 'layoff_watch_youtube_*.csv',
        'reddit_pattern': 'layoff_watch_reddit_*.csv',
        'tiktok_metric': 'layoff_watch'
    },
    'Airline Chaos': {
        'slug': 'airline_chaos',
        'youtube_pattern': 'airline_chaos_youtube_*.csv',
        'reddit_pattern': 'airline_chaos_reddit_*.csv',
        'tiktok_metric': 'airline_chaos'
    }
}

# TikTok combined file pattern
TIKTOK_PATTERN = 'tiktok_youtube_*.csv'

# Per-metric relevance keywords for filtering noisy samples.
# A sample must contain at least one keyword (case-insensitive) to be selected.
RELEVANCE_KEYWORDS = {
    'What Healthcare?': [
        'healthcare', 'health care', 'insurance', 'medical', 'hospital', 'doctor',
        'denied', 'denial', 'prescription', 'drug price', 'copay', 'deductible',
        'prior authorization', 'coverage', 'uninsured', 'bankruptcy', 'medical debt',
        'emergency room', 'ambulance', 'surgery', 'cancer', 'treatment',
    ],
    'AI Psychosis': [
        'ai ', 'a.i.', 'artificial intelligence', 'chatbot', 'chatgpt', 'gpt',
        'replika', 'character.ai', 'companion', 'bot', 'machine learning',
        'deepfake', 'llm', 'openai', 'claude', 'gemini', 'copilot',
        'ai girlfriend', 'ai boyfriend', 'ai addiction', 'ai relationship',
    ],
    'Subscription Overload': [
        'subscription', 'streaming', 'netflix', 'hulu', 'disney+', 'spotify',
        'cancel', 'price hike', 'price increase', 'monthly fee', 'annual fee',
        'saas', 'paywall', 'freemium', 'tier', 'ad-supported', 'subscribe',
    ],
    'Wage Stagnation': [
        'wage', 'salary', 'pay', 'income', 'minimum wage', 'ceo pay',
        'paycheck', 'afford', 'cost of living', 'inflation', 'broke',
        'poverty', 'poor', 'working poor', 'food bank', 'homeless',
        'rent', 'paycheck to paycheck', 'side hustle', 'gig economy',
    ],
    'Housing Despair': [
        'housing', 'house', 'home', 'rent', 'mortgage', 'apartment',
        'evict', 'homeless', 'afford', 'landlord', 'tenant', 'gentrification',
        'down payment', 'real estate', 'housing crisis', 'zoning',
        'first-time buyer', 'homeowner', 'foreclosure', 'shelter',
    ],
    'Dating App Despair': [
        'dating', 'tinder', 'bumble', 'hinge', 'match', 'swipe',
        'relationship', 'single', 'loneliness', 'lonely', 'love',
        'ghosting', 'dating app', 'online dating', 'hookup',
    ],
    'Layoff Watch': [
        'layoff', 'laid off', 'fired', 'job loss', 'unemployment',
        'hiring', 'job search', 'job market', 'resume', 'interview',
        'application', 'rejected', 'recruiter', 'tech layoff', 'downsizing',
        'severance', 'career', 'job seeker', 'talent', 'workforce',
    ],
    'Airline Chaos': [
        'airline', 'flight', 'airport', 'travel', 'delayed', 'cancelled',
        'stranded', 'boarding', 'turbulence', 'faa', 'pilot', 'passenger',
        'baggage', 'lost luggage', 'overbooked', 'spirit', 'delta',
        'united', 'american airlines', 'southwest', 'jetblue',
    ],
}

# Emoji removal regex - covers most common emoji unicode ranges
EMOJI_RE = re.compile(
    '['
    '\U0001F600-\U0001F64F'  # emoticons
    '\U0001F300-\U0001F5FF'  # symbols & pictographs
    '\U0001F680-\U0001F6FF'  # transport & map
    '\U0001F1E0-\U0001F1FF'  # flags
    '\U00002702-\U000027B0'  # dingbats
    '\U000024C2-\U0001F251'  # enclosed characters
    '\U0001F900-\U0001F9FF'  # supplemental symbols
    '\U0001FA00-\U0001FA6F'  # chess symbols
    '\U0001FA70-\U0001FAFF'  # symbols extended-A
    '\U00002600-\U000026FF'  # misc symbols
    '\U0000FE00-\U0000FE0F'  # variation selectors
    '\U0000200D'             # zero width joiner
    '\U00002B50'             # star
    '\U00002B55'             # circle
    '\U000023F0-\U000023FA'  # misc technical
    '\U0000203C-\U00003299'  # CJK and misc
    '\U00002639'             # frowning face
    '\U0000267F'             # wheelchair
    '\U00002702'             # scissors
    '\U00002708'             # airplane
    '\U0000270A-\U0000270D'  # hands
    '\U0000FE0F'             # variation selector
    ']+',
    flags=re.UNICODE
)


def is_relevant(title, metric_name):
    """Check if a title contains at least one relevance keyword for the metric."""
    keywords = RELEVANCE_KEYWORDS.get(metric_name, [])
    if not keywords:
        return True
    title_lower = title.lower()
    return any(kw in title_lower for kw in keywords)


def strip_emoji(text):
    """Remove emoji characters, decode HTML entities, and clean up whitespace."""
    # Decode HTML entities (&#39; -> ', &amp; -> &, etc.)
    cleaned = html.unescape(text)
    # Remove emojis
    cleaned = EMOJI_RE.sub('', cleaned)
    # Collapse multiple spaces into one and strip
    return re.sub(r' +', ' ', cleaned).strip()


def count_data_rows(filepath):
    """Count non-header rows in a CSV file."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            next(reader, None)
            return sum(1 for _ in reader)
    except Exception:
        return 0


def get_latest_file(pattern, min_rows=5):
    """Get the most recent file matching the pattern that has real data."""
    files = glob.glob(os.path.join(DATA_DIR, pattern))
    if not files:
        return None
    # Sort by filename descending (timestamps in filenames ensure chronological order)
    files.sort(reverse=True)
    for filepath in files:
        rows = count_data_rows(filepath)
        if rows >= min_rows:
            return filepath
    return None


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


def select_youtube_samples(data, metric_name, max_samples=2):
    """Select representative YouTube samples prioritizing severity, then engagement.

    Picks from highest severity levels first (L3 > L2 > L1) to ensure
    the most relevant content surfaces over viral but off-topic noise.
    Filters by relevance keywords to exclude noise from broad API searches.
    """
    if not data:
        return []

    # Group by level, sort each group by views
    by_level = {3: [], 2: [], 1: []}
    for row in data:
        category = row.get('category', '')
        level = get_level_from_category(category)
        by_level[level].append(row)

    for level in by_level:
        by_level[level].sort(key=lambda x: int(x.get('view_count', 0) or 0), reverse=True)

    # Pick from L3 first, then L2, then L1
    candidates = by_level[3] + by_level[2] + by_level[1]

    samples = []
    seen_levels = set()

    for row in candidates:
        category = row.get('category', '')
        level = get_level_from_category(category)

        title = strip_emoji(row.get('title', '')[:100])
        if not title:
            continue

        # Filter out off-topic noise
        if not is_relevant(title, metric_name):
            continue

        video_id = row.get('video_id', '')
        url = row.get('url', '')
        if not url and video_id:
            url = f'https://www.youtube.com/watch?v={video_id}'

        # Skip entries with placeholder URLs
        if 'TBD' in video_id or 'TBD' in url:
            continue

        samples.append({
            'content': title,
            'platform': 'youtube',
            'level': level,
            'date': row.get('published_date', row.get('published', ''))[:10],
            'url': url,
            'videoId': video_id,
            'viewCount': int(row.get('view_count', 0) or 0),
            'commentCount': int(row.get('comment_count', row.get('comments', 0)) or 0)
        })
        seen_levels.add(level)

        if len(samples) >= max_samples:
            break

    return samples


def select_reddit_samples(data, metric_name, max_samples=2):
    """Select representative Reddit samples by score, preferring level diversity."""
    if not data:
        return []

    sorted_data = sorted(data, key=lambda x: int(x.get('score', 0) or 0), reverse=True)

    samples = []
    seen_levels = set()

    for row in sorted_data:
        category = row.get('category', '')
        level = get_level_from_category(category)

        if level not in seen_levels or len(samples) < max_samples:
            title = strip_emoji(row.get('title', '')[:100])
            if not title:
                continue

            if not is_relevant(title, metric_name):
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


def select_tiktok_samples(all_tiktok_data, metric_slug, display_name, max_samples=1):
    """Select TikTok samples for a specific metric, prioritizing severity."""
    if not all_tiktok_data:
        return []

    metric_data = [r for r in all_tiktok_data if r.get('metric', '') == metric_slug]
    if not metric_data:
        return []

    # Group by level, sort each group by views
    by_level = {3: [], 2: [], 1: []}
    for row in metric_data:
        level = get_level_from_category(row.get('category', ''))
        by_level[level].append(row)

    for level in by_level:
        by_level[level].sort(key=lambda x: int(x.get('views', 0) or 0), reverse=True)

    candidates = by_level[3] + by_level[2] + by_level[1]

    samples = []
    for row in candidates:
        title = strip_emoji(row.get('title', '')[:100])
        if not title:
            continue

        if not is_relevant(title, display_name):
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

        if len(samples) >= max_samples:
            break

    return samples


def select_hn_samples(data, metric_name, max_samples=1):
    """Select representative Hacker News samples, prioritizing severity then points."""
    if not data:
        return []

    by_level = {3: [], 2: [], 1: []}
    for row in data:
        level = get_level_from_category(row.get('category', ''))
        by_level[level].append(row)

    for level in by_level:
        by_level[level].sort(key=lambda x: int(x.get('points', 0) or 0), reverse=True)

    candidates = by_level[3] + by_level[2] + by_level[1]

    samples = []
    for row in candidates:
        title = strip_emoji(row.get('title', '')[:100])
        if not title:
            continue

        if not is_relevant(title, metric_name):
            continue

        samples.append({
            'content': title,
            'platform': 'hackernews',
            'level': get_level_from_category(row.get('category', '')),
            'date': row.get('created_date', row.get('date', ''))[:10],
            'url': row.get('url', '')
        })

        if len(samples) >= max_samples:
            break

    return samples


def select_cfpb_samples(data, max_samples=1):
    """Select representative CFPB complaint samples."""
    if not data:
        return []

    samples = []
    seen_levels = set()

    for row in data:
        category = row.get('category', '')
        level = get_level_from_category(category)

        if level not in seen_levels or len(samples) < max_samples:
            title = strip_emoji(row.get('title', row.get('narrative', ''))[:100])
            if not title:
                continue

            samples.append({
                'content': title,
                'platform': 'cfpb',
                'level': level,
                'date': row.get('date_received', row.get('date', ''))[:10],
                'url': row.get('url', '')
            })
            seen_levels.add(level)

            if len(samples) >= max_samples:
                break

    return samples


def format_sample_for_ts(sample):
    """Format a sample dict as TypeScript object string."""
    lines = ['      {']

    # Content (escape quotes and backslashes)
    content = sample.get('content', '').replace('\\', '\\\\').replace('"', '\\"')
    lines.append(f'        content: "{content}",')
    lines.append(f'        platform: "{sample.get("platform", "")}",')
    lines.append(f'        level: {sample.get("level", 1)},')
    lines.append(f'        date: "{sample.get("date", "")}",')

    url = sample.get('url', '')
    # Optional fields for YouTube/TikTok
    if sample.get('videoId'):
        lines.append(f'        url: "{url}",')
        lines.append(f'        videoId: "{sample.get("videoId")}",')
        lines.append(f'        viewCount: {sample.get("viewCount", 0)},')
        lines.append(f'        commentCount: {sample.get("commentCount", 0)}')
    else:
        lines.append(f'        url: "{url}"')

    lines.append('      }')
    return '\n'.join(lines)


def find_sample_data_range(content, metric_name):
    """Find the start and end positions of the sampleData array for a metric.

    Returns (start, end) positions of the array contents (between [ and ]),
    or None if not found.
    """
    # Find the metric's title declaration
    title_pattern = f'title: "{re.escape(metric_name)}"'
    title_match = re.search(title_pattern, content)
    if not title_match:
        return None

    # From title position, find sampleData: [
    search_start = title_match.end()
    sample_marker = 'sampleData: ['
    marker_pos = content.find(sample_marker, search_start)
    if marker_pos == -1:
        return None

    # Make sure this sampleData belongs to this metric (not the next one)
    # Check there's no other metric title between our title and sampleData
    next_title = re.search(r'title: "[^"]+",\s*score:', content[search_start + 1:])
    if next_title and (search_start + 1 + next_title.start()) < marker_pos:
        return None

    array_start = marker_pos + len(sample_marker)

    # Find matching ] by counting brackets
    depth = 1
    pos = array_start
    while pos < len(content) and depth > 0:
        if content[pos] == '[':
            depth += 1
        elif content[pos] == ']':
            depth -= 1
        pos += 1

    if depth != 0:
        return None

    array_end = pos - 1  # position of the ]
    return (array_start, array_end)


def update_metric_samples(content, metric_name, samples):
    """Update the sampleData array for a metric in the TypeScript content."""
    if not samples:
        return content

    result = find_sample_data_range(content, metric_name)
    if result is None:
        print(f"  WARNING: Could not find sampleData for {metric_name}")
        return content

    array_start, array_end = result

    # Format samples as TypeScript
    samples_ts = ',\n'.join(format_sample_for_ts(s) for s in samples)

    # Replace the array contents
    new_content = content[:array_start] + '\n' + samples_ts + '\n    ' + content[array_end:]

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
        slug = config['slug']

        # Get latest data files
        youtube_file = get_latest_file(config['youtube_pattern'])
        reddit_file = get_latest_file(config['reddit_pattern'])
        hn_file = get_latest_file(f'{slug}_hackernews_*.csv')
        cfpb_file = get_latest_file(f'{slug}_cfpb_*.csv')

        youtube_data = read_csv_data(youtube_file) if youtube_file else []
        reddit_data = read_csv_data(reddit_file) if reddit_file else []
        hn_data = read_csv_data(hn_file) if hn_file else []
        cfpb_data = read_csv_data(cfpb_file) if cfpb_file else []

        print(f"  YouTube: {len(youtube_data)} entries")
        print(f"  Reddit: {len(reddit_data)} entries")
        print(f"  HN: {len(hn_data)} entries")
        print(f"  CFPB: {len(cfpb_data)} entries")

        # Select samples: 2 YouTube + 2 Reddit + 1 TikTok + 1 HN/CFPB = up to 6
        samples = []
        samples.extend(select_youtube_samples(youtube_data, metric_name, max_samples=2))
        samples.extend(select_reddit_samples(reddit_data, metric_name, max_samples=2))
        samples.extend(select_tiktok_samples(all_tiktok_data, config['tiktok_metric'], metric_name, max_samples=1))

        # Add HN or CFPB sample if available
        if hn_data:
            samples.extend(select_hn_samples(hn_data, metric_name, max_samples=1))
        elif cfpb_data:
            samples.extend(select_cfpb_samples(cfpb_data, max_samples=1))

        # Deduplicate by content (case-insensitive)
        seen_content = set()
        deduped = []
        for s in samples:
            key = s['content'].lower().strip()
            if key not in seen_content:
                seen_content.add(key)
                deduped.append(s)
        samples = deduped

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
