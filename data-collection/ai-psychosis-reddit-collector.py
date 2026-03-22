#!/usr/bin/env python3
"""Reddit collector - AI Psychosis"""

from reddit_collector_base import run_collection

SUBREDDITS = [
    'replika', 'CharacterAI', 'artificial', 'ChatGPT', 'LongDistance',
]

SEARCH_TERMS = [
    'AI companion', 'chatbot relationship', 'replika love',
    'character.ai attachment', 'AI friend', 'emotional support AI',
    'AI addiction', "can't stop talking",
]

LEVEL_3_KEYWORDS = [
    'addiction', 'dependent', "can't stop", 'obsessed', 'real relationship',
    'prefer AI', 'only friend', 'suicidal', 'isolated', 'withdrawn',
    'lost job', 'failing school', 'destroying life', 'intervention',
    'therapy for', 'family worried', 'spending all time',
]

LEVEL_2_KEYWORDS = [
    'attached', 'hours daily', 'replacing friends', 'emotional support',
    'better than real', 'understand me', 'lonely', 'depressed',
    'social anxiety', 'hard to stop', 'checking constantly',
    'miss my AI', 'real feelings', 'in love', 'jealous',
]

LEVEL_3_PHRASES = [
    'destroying my life', 'only friend left', 'prefer ai to people',
    "can't stop using", 'addicted to', 'intervention needed',
]

LEVEL_2_PHRASES = [
    'in love with', 'emotional support', 'better than real',
    'attached to', 'miss my ai', 'hours every day',
]

if __name__ == '__main__':
    run_collection(
        'ai_psychosis', 'AI PSYCHOSIS DATA COLLECTION',
        SUBREDDITS, SEARCH_TERMS,
        LEVEL_3_KEYWORDS, LEVEL_2_KEYWORDS,
        LEVEL_3_PHRASES, LEVEL_2_PHRASES,
    )
