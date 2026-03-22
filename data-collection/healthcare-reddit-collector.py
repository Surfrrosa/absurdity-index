#!/usr/bin/env python3
"""Reddit collector - Healthcare (What Healthcare?)"""

from reddit_collector_base import run_collection

SUBREDDITS = [
    'HealthInsurance', 'Insurance', 'povertyfinance',
    'ChronicIllness', 'diabetes', 'cancer',
]

SEARCH_TERMS = [
    'claim denied', "can't afford treatment", 'prior authorization',
    'medical debt', "insurance won't cover", 'appeal denied',
    'out of network', 'surprise bill',
]

LEVEL_3_KEYWORDS = [
    'bankruptcy', 'collections', 'medical debt', 'going broke',
    "can't afford treatment", 'life-saving', 'cancer treatment',
    'dying', 'emergency', 'life or death', 'denied life-saving',
    'denied cancer treatment', 'filed for bankruptcy',
]

LEVEL_2_KEYWORDS = [
    'denied', 'claim denied', 'rejected', 'appeal denied',
    "won't cover", "can't afford", 'prior authorization',
    "can't afford insulin", 'high deductible', 'out of pocket',
    'surprise bill', 'out of network',
]

LEVEL_3_PHRASES = [
    'filed for bankruptcy', 'going to die', 'denied life-saving',
    "can't afford cancer", 'medical bankruptcy',
]

LEVEL_2_PHRASES = [
    'claim denied', 'appeal denied', 'prior authorization',
    "can't afford", "won't cover",
]

if __name__ == '__main__':
    run_collection(
        'healthcare', 'HEALTHCARE DATA COLLECTION',
        SUBREDDITS, SEARCH_TERMS,
        LEVEL_3_KEYWORDS, LEVEL_2_KEYWORDS,
        LEVEL_3_PHRASES, LEVEL_2_PHRASES,
    )
