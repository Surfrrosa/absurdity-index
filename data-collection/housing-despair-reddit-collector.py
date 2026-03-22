#!/usr/bin/env python3
"""Reddit collector - Housing Despair"""

from reddit_collector_base import run_collection

SUBREDDITS = [
    'FirstTimeHomeBuyer', 'RealEstate', 'povertyfinance',
    'LateStageCapitalism', 'personalfinance', 'Renters',
]

SEARCH_TERMS = [
    "can't afford house", 'gave up homeownership', 'rent increase',
    'eviction', 'deposit impossible', 'outbid again',
    'housing crisis', 'priced out',
]

LEVEL_3_KEYWORDS = [
    'homeless', 'eviction', 'evicted', 'living in car', 'couch surfing',
    'shelter', 'kicked out', '30 day notice', "can't find anywhere",
    'nowhere to go', 'sleeping in', 'tent', 'streets', 'losing home',
    'foreclosure', 'bankruptcy', 'breaking point',
]

LEVEL_2_KEYWORDS = [
    "can't afford", 'priced out', 'rent increase', 'outbid',
    'gave up', 'impossible', 'rejected application', 'no hope',
    'deposit too high', 'bad credit', 'income requirement',
    'moving back home', 'roommates', 'struggling', 'desperate',
]

LEVEL_3_PHRASES = [
    'facing eviction', 'being evicted', 'about to be homeless',
    'living in car', 'nowhere to go', 'kicked out',
    'sleeping in car', 'lost my home',
]

LEVEL_2_PHRASES = [
    "can't afford", 'priced out', 'gave up',
    'rent increase', 'outbid again', 'rejected application',
    'deposit impossible', 'moving back with parents',
]

if __name__ == '__main__':
    run_collection(
        'housing_despair', 'HOUSING DESPAIR DATA COLLECTION',
        SUBREDDITS, SEARCH_TERMS,
        LEVEL_3_KEYWORDS, LEVEL_2_KEYWORDS,
        LEVEL_3_PHRASES, LEVEL_2_PHRASES,
    )
