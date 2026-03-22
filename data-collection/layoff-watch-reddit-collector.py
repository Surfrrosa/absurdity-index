#!/usr/bin/env python3
"""Reddit collector - Layoff Watch"""

from reddit_collector_base import run_collection

SUBREDDITS = [
    'jobs', 'careerguidance', 'cscareerquestions',
    'resumes', 'Layoffs', 'recruitinghell',
]

SEARCH_TERMS = [
    'laid off', 'job search nightmare', '500 applications',
    'no responses', 'overqualified', 'age discrimination',
    'layoff anxiety', 'unemployed months',
]

LEVEL_3_KEYWORDS = [
    'homeless', 'eviction', 'bankruptcy', 'suicide', 'giving up',
    "can't afford food", 'lost everything', 'health insurance',
    'medical emergency', 'breaking point', 'months unemployed',
    'year unemployed', 'savings gone', 'living in car', 'desperate',
]

LEVEL_2_KEYWORDS = [
    'laid off', 'unemployed', 'job search', 'no responses', 'ghosted',
    'rejected', '100 applications', '500 applications', 'overqualified',
    'age discrimination', 'discouraged', 'anxious', 'stressed',
    'running out of money', 'savings dwindling', 'unemployment benefits',
]

LEVEL_3_PHRASES = [
    'facing eviction', 'about to be homeless', "can't afford food",
    'lost health insurance', 'suicidal thoughts', 'lost everything',
    'year unemployed', '18 months', 'savings gone', 'giving up',
]

LEVEL_2_PHRASES = [
    'laid off', '500 applications', 'no responses',
    'months unemployed', 'job search nightmare', 'overqualified',
    'age discrimination', 'ghosted by recruiters',
]

if __name__ == '__main__':
    run_collection(
        'layoff_watch', 'LAYOFF WATCH DATA COLLECTION',
        SUBREDDITS, SEARCH_TERMS,
        LEVEL_3_KEYWORDS, LEVEL_2_KEYWORDS,
        LEVEL_3_PHRASES, LEVEL_2_PHRASES,
    )
