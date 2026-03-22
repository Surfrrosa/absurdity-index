#!/usr/bin/env python3
"""Reddit collector - Subscription Overload"""

from reddit_collector_base import run_collection

SUBREDDITS = [
    'Frugal', 'povertyfinance', 'personalfinance', 'cordcutters',
    'netflix', 'streaming', 'hulu', 'DisneyPlus', 'HBOMAX',
    'Spotify', 'assholedesign', 'mildlyinfuriating', 'NoStupidQuestions',
]

SEARCH_TERMS = [
    'subscription fatigue', 'too many subscriptions', 'canceling subscriptions',
    'subscription audit', "can't afford streaming", 'subscription trap',
    'price increase', 'forgot subscription', 'streaming fatigue',
    'cancel netflix', 'cancel hulu', 'cancel spotify',
    'subscription creep', 'nickel and dime', 'raised prices again',
    'paying for subscriptions', 'subscription hell', 'cutting subscriptions',
]

LEVEL_3_KEYWORDS = [
    'bankruptcy', 'collections', "can't afford", 'homeless', 'eviction',
    'choosing between', 'need food', 'overdraft', 'maxed out',
    'shut off', 'disconnected', 'poverty', 'desperate', 'breaking point',
]

LEVEL_2_KEYWORDS = [
    'price increase', 'cancelled all', "can't keep up", 'budgeting',
    'cutting back', 'too expensive', 'losing track', 'forgot about',
    'hidden fees', 'auto-renewal', 'subscription hell', 'endless',
    'nickeled and dimed', 'overwhelming', 'fatigue',
]

LEVEL_3_PHRASES = [
    "can't afford food", 'choosing between subscriptions and',
    'maxed out credit', 'facing eviction', 'collections calling',
]

LEVEL_2_PHRASES = [
    'cancelled all', 'subscription fatigue', 'price increase',
    'too many subscriptions', "can't keep track", 'overwhelmed',
]

if __name__ == '__main__':
    run_collection(
        'subscription_overload', 'SUBSCRIPTION OVERLOAD DATA COLLECTION',
        SUBREDDITS, SEARCH_TERMS,
        LEVEL_3_KEYWORDS, LEVEL_2_KEYWORDS,
        LEVEL_3_PHRASES, LEVEL_2_PHRASES,
    )
