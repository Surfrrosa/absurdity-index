#!/usr/bin/env python3
"""Reddit collector - Airline Chaos"""

from reddit_collector_base import run_collection

SUBREDDITS = [
    'travel', 'flights', 'delta', 'united', 'americanairlines', 'TravelHacks',
]

SEARCH_TERMS = [
    'flight canceled', 'stranded airport', 'lost luggage',
    'missed connection', 'airline nightmare', 'no compensation',
    'customer service hell', 'delayed hours',
]

LEVEL_3_KEYWORDS = [
    'stranded', 'medical emergency', 'funeral', 'wedding', 'interview',
    'no hotel', 'sleeping in airport', 'stuck for days', 'lost medication',
    'diabetic', 'insulin', 'missing life event', 'job offer',
    'days without luggage', "can't get home", 'desperate', 'breaking point',
]

LEVEL_2_KEYWORDS = [
    'canceled', 'delayed', 'lost luggage', 'missed connection', 'nightmare',
    'hours delayed', 'no compensation', 'customer service', 'refused',
    'stranded', 'stuck', 'ruined trip', 'wasted money', 'no refund',
    'unresponsive', 'ignored', 'frustrated', 'exhausted',
]

LEVEL_3_PHRASES = [
    'missed funeral', 'missed wedding', 'lost medication',
    'sleeping in airport', 'stranded for days', 'medical emergency',
    'stuck for 3 days', "can't get home", 'no insulin',
]

LEVEL_2_PHRASES = [
    'flight canceled', 'lost luggage', 'missed connection',
    'airline nightmare', 'no compensation', 'hours delayed',
    'customer service hell', 'stranded',
]

if __name__ == '__main__':
    run_collection(
        'airline_chaos', 'AIRLINE CHAOS DATA COLLECTION',
        SUBREDDITS, SEARCH_TERMS,
        LEVEL_3_KEYWORDS, LEVEL_2_KEYWORDS,
        LEVEL_3_PHRASES, LEVEL_2_PHRASES,
    )
