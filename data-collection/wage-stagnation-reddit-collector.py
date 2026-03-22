#!/usr/bin/env python3
"""Reddit collector - Wage Stagnation"""

from reddit_collector_base import run_collection

SUBREDDITS = [
    'antiwork', 'WorkReform', 'povertyfinance',
    'LateStageCapitalism', 'jobs', 'Economy',
]

SEARCH_TERMS = [
    'paycheck to paycheck', "can't afford food", 'wages not keeping up',
    'working poor', 'side hustle required', 'three jobs',
    'inflation eating paycheck', 'no savings',
]

LEVEL_3_KEYWORDS = [
    'homeless', 'eviction', 'starving', "can't afford food", 'medical emergency',
    'choosing between', 'skipping meals', 'living in car', 'couch surfing',
    'bankruptcy', 'suicide', 'breaking point', 'lost everything',
    "can't take it anymore", 'giving up', 'no way out',
]

LEVEL_2_KEYWORDS = [
    'paycheck to paycheck', 'no savings', 'overdraft', 'late on rent',
    'credit card debt', "can't afford", 'side hustle', 'second job',
    'third job', 'exhausted', 'burned out', 'drowning', 'struggling',
    'barely making it', 'behind on bills', 'inflation',
]

LEVEL_3_PHRASES = [
    'living in car', 'facing eviction', "can't afford food",
    'choosing between food and', 'suicidal', 'lost everything',
    'about to be homeless', 'skipping meals',
]

LEVEL_2_PHRASES = [
    'paycheck to paycheck', 'three jobs', 'side hustle',
    "can't save", 'drowning in debt', 'barely making it',
    'behind on rent', 'working poor',
]

if __name__ == '__main__':
    run_collection(
        'wage_stagnation', 'WAGE STAGNATION DATA COLLECTION',
        SUBREDDITS, SEARCH_TERMS,
        LEVEL_3_KEYWORDS, LEVEL_2_KEYWORDS,
        LEVEL_3_PHRASES, LEVEL_2_PHRASES,
    )
