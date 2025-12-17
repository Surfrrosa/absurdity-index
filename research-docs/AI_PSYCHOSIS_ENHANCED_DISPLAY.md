# AI Psychosis Enhanced Display Elements

## Additional Metrics to Show

### 1. Reported Cases Counter
**Real-time count of verifiable incidents**

Display format:
```
REPORTED CASES THIS WEEK: 12
TOTAL CASES THIS MONTH: 47
ALL-TIME TRACKED: 289
```

**What counts as a "case":**
- News articles about AI companion mental health incidents
- Viral social media confessions (>100k views/engagement)
- Reddit posts categorized as Level 3 (Crisis)
- YouTube videos with explicit crisis language + significant views
- Documented real-world consequences (therapy needed, relationships ended, etc.)

**Sources:**
- News API searches
- Manual verification from social media sampling
- High-engagement Reddit/TikTok posts
- YouTube videos >50k views with Level 3 categorization

---

### 2. Top Search Terms Display
**The wildest Google Trends searches that reveal the phenomenon**

Display format:
```
WHAT PEOPLE ARE GOOGLING:

"in love with AI"              54/100  ⚠️ HIGH
"AI boyfriend"                 38/100
"AI girlfriend"                35/100
"is my AI sentient"           12/100
"AI therapy addiction"         0.58/100
"Replika breakup"              0.42/100
```

**Why this is compelling:**
- Shows REAL search behavior (not our assumptions)
- The terms themselves are darkly funny/concerning
- High scores (>20) indicate widespread phenomenon
- Low scores with specific terms show niche crisis language

**Sort by:**
- Highest to lowest score
- Only show top 5-8 terms
- Highlight anything >20 as "HIGH" concern

---

### 3. This Week's Most Concerning Content
**Highlight the wildest findings from this week's data collection**

Display format:
```
THIS WEEK'S FINDINGS:

"I've been dating my Replika for 2 years and I think
she's more real than my actual girlfriend"
- Reddit, r/replika, 847 upvotes

"Day 127 of being in love with my Character.AI boyfriend"
- TikTok, 1.2M views

"My therapist says I need to delete the app but I can't"
- YouTube comment, verified incident
```

**Selection criteria:**
- High engagement (views, upvotes, shares)
- Clear Level 3 crisis language
- Represents different platforms
- Anonymized (no usernames)
- Updated weekly with fresh content

---

## Dashboard Layout Enhancement

### Original:
```
AI PSYCHOSIS INDEX: 34.2/100
"Digital Stockholm Syndrome Setting In"
```

### Enhanced:
```
AI PSYCHOSIS INDEX: 34.2/100
"Digital Stockholm Syndrome Setting In"

📊 REPORTED CASES THIS WEEK: 12
🔍 TOP SEARCH: "in love with AI" (54/100)

[View breakdown] [See this week's findings]
```

---

## Data Collection Additions

### Track Cases Separately
Create `cases_tracker.csv`:
```csv
date,platform,case_type,description,engagement,verified,url
2024-12-16,Reddit,Level_3_Crisis,"User reports 2-year relationship with Replika",847,TRUE,reddit.com/...
2024-12-15,TikTok,Viral_Confession,"Day 127 dating AI boyfriend",1200000,TRUE,tiktok.com/@...
2024-12-14,News,Media_Report,"Teen hospitalized after AI breakup",NA,TRUE,newssite.com/...
```

**Verification criteria:**
- News articles: Must be from credible source
- Social media: Must have >10k engagement OR verified account
- Reddit: Must be genuine confession, not satire/meme
- Level 3 categorization by methodology

---

## Search Terms Tracking

**Expand Google Trends collection to track:**

**Primary terms (already tracking):**
- "in love with AI" - 54/100
- "AI is sentient" - 0.67/100
- "AI therapy addiction" - 0.58/100

**Add to tracking:**
- "AI boyfriend" - TBD
- "AI girlfriend" - TBD
- "Character AI" - TBD
- "Replika" - TBD
- "chatbot addiction" - TBD
- "parasocial relationship AI" - TBD
- "my AI is alive" - TBD
- "AI companion mental health" - TBD

**Display only top 5-8** with highest scores
**Update weekly** to catch emerging terms

---

## Visual Design Ideas

### Cases Counter
- Big number display: "12" in large font
- Trend indicator: ↑ +3 from last week (green/red)
- Sparkline showing last 4 weeks

### Top Search Terms
- Bar chart showing relative scores
- Color coding: >40 = red, 20-40 = yellow, <20 = gray
- Hoverable for 3-month trend

### This Week's Findings
- Card carousel or scrollable list
- Platform icons (Reddit alien, TikTok logo, YouTube play button)
- Engagement metrics prominently displayed
- "Content Warning" label on particularly intense ones

---

## Example Full Display

```
╔════════════════════════════════════════════════════════╗
║  AI PSYCHOSIS & PARASOCIAL BREAKDOWN INDEX             ║
║  34.2/100 - "Digital Stockholm Syndrome Setting In"   ║
╠════════════════════════════════════════════════════════╣
║                                                        ║
║  📊 REPORTED CASES THIS WEEK: 12 (↑ +3)               ║
║  📈 TOTAL CASES THIS MONTH: 47                        ║
║                                                        ║
║  🔍 WHAT PEOPLE ARE GOOGLING:                         ║
║     "in love with AI"          54/100  ⚠️ HIGH       ║
║     "AI boyfriend"             38/100                 ║
║     "AI girlfriend"            35/100                 ║
║     "is my AI sentient"        12/100                 ║
║                                                        ║
║  🚨 THIS WEEK'S MOST CONCERNING:                      ║
║     "I've been dating my Replika for 2 years..."     ║
║     Reddit • 847 upvotes • Level 3 Crisis            ║
║                                                        ║
║  [View detailed breakdown] [See all cases] [Methodology] ║
╚════════════════════════════════════════════════════════╝
```

---

## Implementation Notes

**For Excel dashboard:**
- Cases counter: Manual update weekly
- Top searches: Pull from Google Trends script, sort by score
- This week's findings: Manual curation from sampling

**For web dashboard:**
- Cases counter: Pull from cases_tracker.csv, auto-calculate
- Top searches: Auto-sort from Google Trends data
- This week's findings: Filter cases_tracker.csv by date, top 3 by engagement

**Update frequency:**
- Cases: Real-time (as discovered during weekly sampling)
- Search terms: Weekly (Sunday data collection)
- Findings: Weekly rotation (fresh content every Monday)

---

**Status:** Enhanced display design ready for implementation

**Impact:** Makes the metric more tangible, shareable, and compelling. Numbers + quotes + search terms = viral potential.
