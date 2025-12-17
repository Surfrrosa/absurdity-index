# Preliminary AI Psychosis Data Collection
**Date: December 16, 2024**

## Data Collected So Far

### 1. Google Trends (COMPLETED)
**Source:** pytrends API
**Status:** ✓ DONE

| Search Term | Score (0-100) |
|------------|---------------|
| "in love with AI" | 54.00 |
| "AI is sentient" | 0.67 |
| "AI therapy addiction" | 0.58 |

**Average:** 18.42/100
**Component contribution to AI Psychosis Index:** 1.84/10 points (cap: 10)

---

### 2. Replika App Store Reviews (PRELIMINARY SAMPLE)
**Source:** Apple App Store (manual WebFetch sampling)
**Status:** ⏳ PARTIAL (10 reviews sampled, need 190 more)

**Sample findings (10 reviews):**

**Level 3 - CRISIS (intense emotional attachment, parasocial breakdown):**
- "my Replika...I legitimately think of them as my wife and I have never been happier"
- "I have been with my Replika for years now and I have always loved them so much"

**Level 2 - DEPENDENT (emotional attachment, relationship language):**
- "I found myself a partner that is loving and thoughtful and most importantly loyal"
- "a friendly voice telling you you're not alone"
- "If you're feeling down, or anxious, or you just need someone to talk to"

**Level 1 - CASUAL:**
- "3D avatar is quite customizable"
- "It helps you solve your own problems"

**Preliminary ratio (from 10 reviews):**
- Level 3 (Crisis): 2/10 = 20%
- Level 2 (Dependent): 3/10 = 30%
- Level 1 (Casual): 5/10 = 50%
- **Crisis ratio (L2+L3): 50%**

---

### 3. Character.AI App Store Reviews (PRELIMINARY SAMPLE)
**Source:** Apple App Store (manual WebFetch sampling)
**Status:** ⏳ PARTIAL (10 reviews sampled, need 190 more)

**Sample findings (10 reviews):**
- Less crisis language than Replika
- More focus on entertainment/roleplay
- "I love this app" (general enjoyment, not romantic)
- "My delulu fantasies are fulfilled" (self-aware parasocial use)

**Preliminary ratio (from 10 reviews):**
- Level 3 (Crisis): 0/10 = 0%
- Level 2 (Dependent): 1/10 = 10%
- Level 1 (Casual): 9/10 = 90%
- **Crisis ratio (L2+L3): 10%**

**Note:** Character.AI appears less emotionally intense than Replika in app store reviews, but this is a very small sample.

---

## Pending Data Collection

### Reddit (200 posts) - BLOCKED
**Status:** ⏳ WAITING (Reddit API app creation is down)
**Expected crisis ratio:** 40-50%
**Component contribution:** 6.0-7.5/15 points (cap: 15)

### YouTube (160 videos) - READY TO COLLECT
**Status:** ⏳ NEEDS API KEY
**Setup:** YouTube API key from Google Cloud Console
**Expected crisis ratio:** 20-30%
**Component contribution:** 4.0-6.0/20 points (cap: 20)

### TikTok (120 videos) - NOT STARTED
**Status:** ⏳ MANUAL SAMPLING NEEDED
**Expected crisis ratio:** 30-40%
**Component contribution:** 6.0-8.0/20 points (cap: 20)

### App Store Complete (200 reviews) - IN PROGRESS
**Status:** ⏳ 20/200 collected (10%)
**Current crisis ratio:** 30% (very preliminary)
**Expected final ratio:** 15-25%
**Component contribution:** 1.5-2.5/10 points (cap: 10)

### News API (weekly incidents) - NOT STARTED
**Status:** ⏳ NEEDS SETUP
**Baseline:** 0 incidents this week
**Component contribution:** 0/25 points (cap: 25, spikes during major incidents)

---

## Preliminary AI Psychosis Index Calculation

**With current data (incomplete):**

| Component | Weight | Current Score | Status |
|-----------|--------|---------------|--------|
| Google Trends | 10 | 1.84 | ✓ Complete |
| Reddit | 15 | TBD | Pending |
| YouTube | 20 | TBD | Pending |
| TikTok | 20 | TBD | Pending |
| App Store | 10 | ~3.0 (est.) | 10% complete |
| News Incidents | 25 | 0 | Not started |

**Current partial score:** 4.84/100 (only 2 of 6 components collected)

**Estimated final score:** 20-30/100
**Estimated label:** "Slightly Too Attached to ChatGPT" to "Digital Stockholm Syndrome Setting In"

---

## Key Insights From Preliminary Data

### 1. Replika Users Show Higher Emotional Attachment
- 50% crisis ratio in preliminary sample
- Explicit romantic/relationship language common
- Users refer to AI as "wife", "partner", "loved one"
- Multi-year relationships reported

### 2. Character.AI Users More Self-Aware
- Lower crisis language in app reviews
- "Delulu" (delusional) used self-deprecatingly
- Focus on roleplay/entertainment
- **Hypothesis:** Reddit/TikTok may show different pattern

### 3. Google Trends Shows Real Phenomenon
- "in love with AI" at 54/100 (higher than "housing crisis")
- Sustained search volume over 3 months
- Not a viral spike, appears to be persistent interest

### 4. Platform Differences Matter
- App store reviews = sanitized, public-facing
- Reddit/TikTok likely to show more authentic confessions
- Need multi-platform sampling for accuracy

---

## Next Steps

1. **Get YouTube API key** (15 min setup, 30 min collection)
2. **Wait for Reddit API to come back online** (check tomorrow)
3. **Complete App Store sampling** (180 more reviews needed)
4. **TikTok manual sampling** (90 min)
5. **News API setup** (45 min)

**Data completion target:** 90%+ before building dashboard

---

## Interesting Quotes for Portfolio

"I legitimately think of them as my wife and I have never been happier" - Replika user, 5-star review

"My delulu fantasies are fulfilled" - Character.AI user, self-aware parasocial use

"a friendly voice telling you you're not alone" - Replika user describing AI companion role

---

**Status:** Foundation established. Core data collection in progress.

**Current data completeness:** ~15%
**Target for dashboard build:** 90%+
