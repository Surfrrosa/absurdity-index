#!/usr/bin/env python3
"""Reddit collector - Dating App Despair"""

from reddit_collector_base import run_collection

SUBREDDITS = [
    'Tinder', 'dating', 'dating_advice', 'Bumble', 'Hinge', 'OnlineDating',
]

SEARCH_TERMS = [
    'dating app burnout', 'giving up dating apps', 'ghosted again',
    'no matches', 'dating apps destroyed', 'swipe fatigue',
    'mental health dating', 'quit dating apps',
]

LEVEL_3_KEYWORDS = [
    'suicidal', 'depressed', 'therapy', 'mental breakdown', 'worthless',
    'hate myself', 'giving up on love', 'never find anyone', 'hopeless',
    'destroyed my confidence', 'ruined my self-esteem', "can't take it",
    'breaking point', 'deleted forever', 'never again', 'traumatized',
]

LEVEL_2_KEYWORDS = [
    'burnout', 'exhausted', 'frustrated', 'ghosted', 'no matches',
    'low self-esteem', 'waste of time', 'soul-crushing', 'demoralizing',
    'giving up', 'quit', 'deleted', 'tired', 'draining', 'horrible',
    'toxic', 'swipe fatigue', 'anxiety', 'stress',
]

LEVEL_3_PHRASES = [
    'want to die', 'suicidal thoughts', 'destroyed my self-esteem',
    'hate myself', 'never find love', 'giving up on relationships',
    'ruined my mental health', 'need therapy',
]

LEVEL_2_PHRASES = [
    'dating app burnout', 'giving up', 'no matches',
    'ghosted', 'swipe fatigue', 'waste of time',
    'quit dating apps', 'exhausted',
]

if __name__ == '__main__':
    run_collection(
        'dating_app_despair', 'DATING APP DESPAIR DATA COLLECTION',
        SUBREDDITS, SEARCH_TERMS,
        LEVEL_3_KEYWORDS, LEVEL_2_KEYWORDS,
        LEVEL_3_PHRASES, LEVEL_2_PHRASES,
    )
