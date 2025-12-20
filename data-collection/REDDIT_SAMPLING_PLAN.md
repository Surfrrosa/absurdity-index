# Reddit Sampling Plan

**Last Updated:** December 20, 2025
**Status:** PENDING - Awaiting Reddit API approval
**Purpose:** Medium-priority social sentiment data collection across all metrics

---

## Overview

Reddit provides richer, longer-form content than YouTube titles/descriptions. Users share detailed personal experiences, making it ideal for categorizing Level 1/2/3 severity.

**Target:** 200 posts per metric
**Total target:** 1,600 posts across 8 metrics

---

## API Access Requirements

### Current Status
- **Reddit API application:** Submitted, awaiting approval
- **Expected timeline:** 2-4 weeks
- **API tier needed:** Developer (free tier should suffice for our volume)

### API Credentials Needed
```
client_id: [pending]
client_secret: [pending]
user_agent: absurdity-index-data-collector/1.0
```

### Rate Limits
- Free tier: 60 requests/minute
- Our needs: ~10 requests/metric (20 search terms × 20-30 posts each)
- Should complete within limits using sleep timers

---

## Sampling Methodology

### Subreddit Selection

For each metric, target 3-5 relevant subreddits:

#### 1. What Healthcare?
**Subreddits:**
- r/HealthInsurance (~200k members) - 50 posts
- r/Insurance (~100k members) - 30 posts
- r/povertyfinance (~1.5M members) - 40 posts
- r/ChronicIllness (~200k members) - 30 posts
- r/diabetes (~400k members) - 25 posts
- r/cancer (~100k members) - 25 posts

**Search terms:**
- "claim denied"
- "can't afford treatment"
- "prior authorization"
- "medical debt"
- "insurance won't cover"
- "appeal denied"
- "out of network"
- "surprise bill"

**Sampling:** Sort by 'top' (past month), collect systematically

---

#### 2. AI Psychosis
**Subreddits:**
- r/replika (~150k members) - 70 posts
- r/CharacterAI (~100k members) - 60 posts
- r/artificial (~500k members) - 30 posts
- r/ChatGPT (~3M members) - 20 posts
- r/LongDistance (for AI relationship content) - 20 posts

**Search terms:**
- "AI companion"
- "chatbot relationship"
- "replika love"
- "character.ai attachment"
- "AI friend"
- "emotional support AI"
- "AI addiction"
- "can't stop talking"

**Sampling:** Sort by 'hot' and 'top' (past 3 months)

---

#### 3. Subscription Overload
**Subreddits:**
- r/Frugal (~3M members) - 50 posts
- r/povertyfinance (~1.5M members) - 40 posts
- r/personalfinance (~18M members) - 40 posts
- r/cordcutters (~300k members) - 35 posts
- r/netflix (~3M members) - 20 posts
- r/streaming (~50k members) - 15 posts

**Search terms:**
- "subscription fatigue"
- "too many subscriptions"
- "canceling subscriptions"
- "subscription audit"
- "can't afford streaming"
- "subscription trap"
- "price increase"
- "forgot subscription"

**Sampling:** Sort by 'top' (past month)

---

#### 4. Wage Stagnation
**Subreddits:**
- r/antiwork (~2M members) - 50 posts
- r/WorkReform (~500k members) - 40 posts
- r/povertyfinance (~1.5M members) - 40 posts
- r/LateStageCapitalism (~1M members) - 35 posts
- r/jobs (~500k members) - 20 posts
- r/Economy (~300k members) - 15 posts

**Search terms:**
- "paycheck to paycheck"
- "can't afford food"
- "wages not keeping up"
- "working poor"
- "side hustle required"
- "three jobs"
- "inflation eating paycheck"
- "no savings"

**Sampling:** Sort by 'top' (past month)

---

#### 5. Housing Despair
**Subreddits:**
- r/FirstTimeHomeBuyer (~200k members) - 40 posts
- r/RealEstate (~3M members) - 40 posts
- r/povertyfinance (~1.5M members) - 35 posts
- r/LateStageCapitalism (~1M members) - 30 posts
- r/personalfinance (~18M members) - 30 posts
- r/Renters (~50k members) - 25 posts

**Search terms:**
- "can't afford house"
- "gave up homeownership"
- "rent increase"
- "eviction"
- "deposit impossible"
- "outbid again"
- "housing crisis"
- "priced out"

**Sampling:** Sort by 'top' (past month)

---

#### 6. Dating App Despair
**Subreddits:**
- r/Tinder (~7M members) - 40 posts
- r/dating (~1M members) - 40 posts
- r/dating_advice (~2M members) - 35 posts
- r/Bumble (~500k members) - 25 posts
- r/Hinge (~400k members) - 25 posts
- r/OnlineDating (~300k members) - 35 posts

**Search terms:**
- "dating app burnout"
- "giving up dating apps"
- "ghosted again"
- "no matches"
- "dating apps destroyed"
- "swipe fatigue"
- "mental health dating"
- "quit dating apps"

**Sampling:** Sort by 'top' (past month)

---

#### 7. Layoff Watch
**Subreddits:**
- r/jobs (~500k members) - 50 posts
- r/careerguidance (~800k members) - 40 posts
- r/cscareerquestions (~3M members) - 35 posts
- r/resumes (~300k members) - 30 posts
- r/Layoffs (~50k members) - 25 posts
- r/recruitinghell (~500k members) - 20 posts

**Search terms:**
- "laid off"
- "job search nightmare"
- "500 applications"
- "no responses"
- "overqualified"
- "age discrimination"
- "layoff anxiety"
- "unemployed months"

**Sampling:** Sort by 'top' (past month)

---

#### 8. Airline Chaos
**Subreddits:**
- r/travel (~5M members) - 50 posts
- r/flights (~100k members) - 40 posts
- r/delta (~50k members) - 30 posts
- r/united (~40k members) - 25 posts
- r/americanairlines (~30k members) - 25 posts
- r/TravelHacks (~200k members) - 30 posts

**Search terms:**
- "flight canceled"
- "stranded airport"
- "lost luggage"
- "missed connection"
- "airline nightmare"
- "no compensation"
- "customer service hell"
- "delayed hours"

**Sampling:** Sort by 'hot' and 'top' (past month)

---

## Data Collection Process

### Script Template

```python
import praw
import pandas as pd
from datetime import datetime, timedelta

# Initialize Reddit API
reddit = praw.Reddit(
    client_id='YOUR_CLIENT_ID',
    client_secret='YOUR_CLIENT_SECRET',
    user_agent='absurdity-index-data-collector/1.0'
)

def collect_reddit_posts(subreddit_name, search_terms, num_posts=200):
    """Collect posts from a subreddit matching search terms"""
    subreddit = reddit.subreddit(subreddit_name)
    posts = []

    for term in search_terms:
        # Search subreddit
        for post in subreddit.search(term, time_filter='month', limit=30):
            posts.append({
                'subreddit': subreddit_name,
                'post_id': post.id,
                'title': post.title,
                'selftext': post.selftext[:500],  # First 500 chars
                'url': post.url,
                'score': post.score,
                'num_comments': post.num_comments,
                'created_utc': datetime.fromtimestamp(post.created_utc),
                'search_term': term
            })

    return posts
```

### Categorization Logic

Same 3-level system as YouTube:

**Level 3 (Crisis):**
- 2+ crisis keywords OR
- 1 critical phrase from metric-specific list

**Level 2 (Struggling):**
- 2+ frustration keywords OR
- 1 common frustration phrase

**Level 1 (Aware):**
- Default for relevant content

*See CATEGORIZATION_CRITERIA.md for full keyword lists*

### Data Storage

**File format:** CSV
**Naming:** `{metric}_reddit_{YYYYMMDD_HHMMSS}.csv`
**Location:** `data-collection/collected-data/`

**Columns:**
- subreddit
- post_id
- title
- selftext_snippet
- url
- score (upvotes)
- num_comments
- created_utc
- search_term
- category (LEVEL_1/2/3)
- notes

---

## Quality Control

### Filters

1. **Relevance check:** Manual review of sample (20 posts per metric)
2. **Spam removal:** Filter out promotional posts
3. **Recency:** Posts from last 90 days only
4. **Minimum engagement:** Score >2 or num_comments >1

### Validation

- Inter-coder reliability: Have 2 people categorize same 50 posts
- Target agreement: >80% on Level 2/3 boundary
- Document edge cases

---

## Timeline

### When API Access Granted

**Week 1:**
- Set up API credentials
- Test collection script on 1-2 metrics
- Validate categorization accuracy

**Week 2-3:**
- Collect all 8 metrics (200 posts each)
- Run quality control
- Calculate crisis ratios

**Week 4:**
- Update metric scores with Reddit data
- Compare Reddit vs YouTube sentiment
- Document findings

---

## Expected Outcomes

### Sentiment Comparison

**Hypothesis:** Reddit will show higher crisis ratios than YouTube

**Reasoning:**
- Longer posts allow more detailed struggles
- Anonymity encourages honesty
- Subreddits like r/antiwork skew negative

**Expected ranges:**
- Healthcare: 25-35% crisis (vs 21% YouTube)
- Subscription Overload: 5-15% crisis (vs 1.3% YouTube)
- Wage Stagnation: 40-55% crisis
- Dating App Despair: 35-50% crisis

### Integration

Reddit data will be:
1. **Combined with YouTube:** Weighted average crisis ratio
2. **Analyzed separately:** Platform comparison insights
3. **Used for validation:** Check if YouTube findings hold on Reddit

---

## Blockers & Alternatives

### If Reddit API Denied

**Alternative data sources:**
1. Manual Reddit sampling (scrape 20-30 posts per metric without API)
2. Twitter/X API (if accessible)
3. Increase YouTube/TikTok volume
4. Use public Reddit datasets (if available from academic sources)

### If Rate Limits Too Restrictive

- Collect over multiple days
- Focus on highest-priority metrics first
- Reduce target from 200 → 100 posts per metric

---

## Notes for Implementation

- Reddit content is **much longer** than YouTube titles → better categorization accuracy
- Upvote/comment counts can serve as engagement weights (like view counts)
- Some subreddits have rules against data collection → check before scraping
- Be respectful of rate limits to avoid API ban
