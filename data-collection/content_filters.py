#!/usr/bin/env python3
"""
Shared content filters for data collection scripts.
Filters out clickbait, spam, and promotional content that doesn't represent
genuine experiences.
"""

# Clickbait/spam title patterns (case-insensitive matching)
CLICKBAIT_PATTERNS = [
    # "One trick" type patterns
    "after learning this one",
    "this one rule",
    "this one trick",
    "this one secret",
    "this one simple",
    "one weird trick",
    "secret the banks",
    "banks don't want you to know",
    "they don't want you to know",
    "what they don't tell you",

    # Financial guru sales tactics
    "financial freedom in",
    "get rich",
    "make money fast",
    "passive income secrets",
    "i made $",
    "how i made $",
    "quit my job and now",
    "fire movement success",

    # Self-promotion patterns
    "here's my channel",
    "subscribe for more",
    "link in bio",
    "check out my course",
    "join my program",
    "free webinar",
    "dm me for",

    # Misleading fix promises
    "i stopped living paycheck to paycheck after",
    "i fixed my finances in",
    "debt free in",
    "how i paid off",
    "i saved $",
    "budget hack that",
]

# Channel name patterns to exclude (promotional channels)
PROMO_CHANNEL_PATTERNS = [
    "wealth",
    "money coach",
    "financial advisor",
    "get rich",
    "millionaire",
    "stealth wealth",
]


def is_clickbait(title: str, description: str = "") -> bool:
    """
    Check if content appears to be clickbait or promotional spam.

    Args:
        title: Video/post title
        description: Video/post description (optional)

    Returns:
        True if content appears to be clickbait/spam
    """
    text = (title + " " + description).lower()

    # Check for clickbait patterns
    for pattern in CLICKBAIT_PATTERNS:
        if pattern in text:
            return True

    return False


def is_promotional_channel(channel_name: str) -> bool:
    """
    Check if channel name suggests promotional/guru content.

    Args:
        channel_name: YouTube channel name

    Returns:
        True if channel appears promotional
    """
    channel_lower = channel_name.lower()

    for pattern in PROMO_CHANNEL_PATTERNS:
        if pattern in channel_lower:
            return True

    return False


def filter_content(title: str, description: str = "", channel_name: str = "") -> bool:
    """
    Main filter function - returns True if content should be INCLUDED.

    Args:
        title: Content title
        description: Content description
        channel_name: Source channel/user name

    Returns:
        True if content passes filters (should be included)
        False if content should be filtered out
    """
    if is_clickbait(title, description):
        return False

    if channel_name and is_promotional_channel(channel_name):
        return False

    return True
