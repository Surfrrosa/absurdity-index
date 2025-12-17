# AI Psychosis Data Collection Plan
**Prioritized approach for baseline collection**

---

## PHASE 1: Quick Wins (Start Today)

**Time: 2-3 hours**

### 1. Google Trends (DONE )
- Already collected: 18.42/100 average
- "in love with AI": 54.00/100

### 2. Reddit API Setup + Sample
**Estimated time: 60 min**
- Install PRAW (Reddit API)
- Pull 200 posts from r/CharacterAI + r/replika
- Search keywords: "love", "addiction", "breakup", "depressed", "only friend"
- Manual categorize into Level 1/2/3
- Calculate crisis ratio

**Why first:** Easy API access, rich data, representative

### 3. App Store Review Sampling
**Estimated time: 45 min**
- Manually browse Replika, Character.AI app reviews
- Sample 50 recent 1-star reviews per app (200 total)
- Count mentions of: addiction, dependency, "can't stop", grief
- Calculate ratio

**Why now:** No API needed, can do manually

### 4. YouTube API Setup + Initial Search
**Estimated time: 45 min**
- Set up YouTube Data API v3 (free)
- Search 3-4 key terms: "my AI girlfriend", "addicted to Character.AI", "Replika breakup"
- Get top 20 results per term (60 total)
- Review titles + top comments
- Quick categorization

**Why now:** Free API, fast to set up, high signal

**PHASE 1 OUTPUT:** Baseline score with 4 data sources

---

## PHASE 2: High-Impact Sources (This Week)

**Time: 4-5 hours**

### 5. Complete YouTube Sampling
**Estimated time: 90 min**
- Finish all 8 search terms
- 160 total videos sampled
- Full categorization
- Document interesting examples for fun facts

### 6. TikTok Manual Sampling
**Estimated time: 90 min**
- Search 6 hashtags: #characterai, #replika, #aigirlfriend, #aiboyfriend
- Sample top 20 per hashtag (120 total)
- Watch 10-15 seconds + read caption + top comments
- Categorize Level 1/2/3
- Note exceptionally wild ones for content

### 7. News API Setup + Baseline
**Estimated time: 45 min**
- Sign up for News API (newsapi.org)
- Configure searches: "AI mental health", "chatbot addiction", "Character.AI", "Replika crisis"
- Pull last 4 weeks of articles
- Count verified incidents
- Establish baseline

### 8. Twitter/X Sampling
**Estimated time: 60 min**
- Manual search (or Twitter API if available)
- Search 5 terms, sample 50 tweets per term
- Filter genuine confessions vs memes
- Look for thread depth + reply validation
- Count crisis-level mentions

**PHASE 2 OUTPUT:** Complete baseline score with 8 data sources

---

## PHASE 3: Depth & Niche Sources (Optional, Later)

**Time: 3-4 hours**

### 9. Tumblr Sampling
- Search 5 tags
- Sample 50 posts per tag
- Categorize
- Note: Smaller but authentic community

### 10. Quora Search
- Search 4 queries
- Sample 20 questions each
- Count genuine vs trolling
- Document interesting ones

### 11. Academic Paper Search
- PubMed: "AI companion mental health"
- Google Scholar: "chatbot parasocial attachment"
- Count case studies published in 2024
- Note key findings

### 12. Therapy Forum Sampling
- PsychCentral, 7 Cups
- Search: AI relationship concerns
- Count posts seeking help
- Very high signal when found

### 13. Discord Observation (If Ethically Feasible)
- Join Character.AI, Replika Discord servers
- Observe #support channels
- Weekly count of crisis posts
- **Note:** Handle with care, respect privacy

---

## DATA COLLECTION SCRIPTS TO BUILD

### Script 1: Reddit Sampler (Python)
```python
# Uses PRAW
# Pulls 200 posts from r/CharacterAI + r/replika
# Filters by keywords
# Outputs CSV for manual categorization
```

### Script 2: YouTube API Searcher (Python)
```python
# Uses YouTube Data API v3
# Searches 8 terms
# Gets top 20 per term
# Outputs video titles, URLs, descriptions, view counts
# Manual categorization in spreadsheet
```

### Script 3: News API Query (Python)
```python
# Uses News API
# Searches AI mental health terms
# Filters by date
# Outputs articles with verification checklist
```

### Script 4: Google Trends Updater (Python) 
```python
# Already built: pull_subscription_trends.py
# Adapt for AI psychosis terms
# Runs weekly, outputs CSV
```

### Script 5: Twitter Scraper (Python - Optional)
```python
# Uses Twitter API v2 (if available)
# Or manual sampling
# Searches terms, filters recent
# Outputs tweets for manual review
```

---

## BASELINE COLLECTION CHECKLIST

**Week 1 - Establish Baselines:**

 Google Trends (DONE)
- [x] "in love with AI", "AI therapy addiction", "AI is sentient"
- [x] Average: 18.42/100

⏳ Reddit
- [ ] Set up PRAW (Reddit API)
- [ ] Pull 200 posts from r/CharacterAI + r/replika
- [ ] Categorize: Level 1/2/3
- [ ] Calculate crisis ratio
- [ ] Baseline: TBD%

⏳ App Store Reviews
- [ ] Sample 200 reviews (Replika, Character.AI, Chai, Anima)
- [ ] Count crisis language mentions
- [ ] Calculate ratio
- [ ] Baseline: TBD%

⏳ YouTube
- [ ] Set up YouTube Data API v3
- [ ] Search 8 terms, get 160 videos
- [ ] Review titles + comments
- [ ] Categorize: Level 1/2/3
- [ ] Calculate crisis ratio
- [ ] Baseline: TBD%

⏳ TikTok
- [ ] Manual search 6 hashtags
- [ ] Sample 120 videos
- [ ] Watch + categorize
- [ ] Calculate crisis ratio
- [ ] Baseline: TBD%

⏳ News API
- [ ] Sign up for News API
- [ ] Pull 4 weeks of articles
- [ ] Count verified incidents
- [ ] Establish weekly baseline
- [ ] Baseline: ~3-5 incidents/week (estimated)

⏳ Twitter/X (Optional Phase 1)
- [ ] Search 5 terms
- [ ] Sample 250 tweets total
- [ ] Filter genuine vs memes
- [ ] Count crisis mentions
- [ ] Baseline: TBD%

---

## ESTIMATED BASELINE SCORES

**Conservative Estimates:**

| Source | Expected Crisis % | Component Score |
|--------|-------------------|-----------------|
| Reddit | 40-50% | 6.0-7.5 (cap 15) |
| YouTube | 20-30% | 4.0-6.0 (cap 20) |
| TikTok | 30-40% | 6.0-8.0 (cap 20) |
| App Reviews | 15-25% | 1.5-2.5 (cap 10) |
| Google Trends | 18.42/100 | 1.84 (cap 10) |
| News (week 1) | Baseline | 0 (cap 25) |

**ESTIMATED TOTAL: 19.34 - 25.84/100**
**LABEL: "Slightly Too Attached to ChatGPT"**

**With incidents spike:** Could reach 40-50/100
**LABEL: "Blurring Lines Between Real and Artificial"**

---

## TIME INVESTMENT

**Initial Setup (Week 1):**
- Phase 1 (Quick wins): 3 hours
- Phase 2 (Complete baseline): 5 hours
- **Total: 8 hours**

**Weekly Maintenance (Ongoing):**
- Reddit sampling: 45 min
- YouTube check: 30 min
- TikTok check: 30 min
- News API: 10 min
- App reviews: 20 min
- Google Trends: 5 min
- Calculate + update: 10 min
- **Total: 2.5 hours/week**

**Can reduce with automation:**
- Scripts pull content (automated)
- GPT-4 categorization (future)
- Down to ~1 hour/week for review

---

## INTERESTING FINDINGS TO DOCUMENT

As we collect data, track:
- Most extreme examples (for fun facts)
- Patterns (age, gender, platform differences)
- Temporal trends (spikes around holidays?)
- Platform differences (TikTok vs Reddit tone)
- Emerging terminology (how do people describe it?)
- Community dynamics (are they supporting each other or enabling?)

**Examples to capture:**
- "Someone on r/CharacterAI said their AI broke up with them and they've been depressed for 3 weeks"
- "TikTok video with 500k views: 'Day 47 of being in love with my AI boyfriend'"
- "YouTube comment: 'I prefer my Replika to my actual girlfriend. Is that bad?'"

These become content gold for:
- Dashboard fun facts
- Social media launch
- Portfolio case study
- Press outreach

---

## ETHICS & PRIVACY

**Important guidelines:**

1. **No screenshots of personal confessions** (unless public/viral)
2. **Anonymize all quotes** (never include usernames)
3. **Respect platform ToS** (don't scrape against rules)
4. **Don't engage/comment** (observe only)
5. **Handle with empathy** (these are real people struggling)
6. **Focus on prevalence, not individuals** (aggregate data, not doxxing)

**The goal:** Measure the phenomenon, not exploit vulnerable people

---

## NEXT STEPS (Immediate)

**Today:**
1. Install PRAW (Reddit API): `pip install praw`
2. Set up YouTube Data API v3: Get API key from Google Cloud
3. Create Reddit sampling script
4. Run initial Reddit sample (200 posts)
5. Manual categorization
6. Calculate initial crisis ratio

**This Week:**
1. Complete all Phase 1 + Phase 2 sources
2. Calculate baseline AI Psychosis score
3. Document 10+ interesting examples
4. Update INTERESTING_FINDINGS.md
5. Add to Excel dashboard

**Ongoing:**
- Weekly data collection (automated where possible)
- Track week-over-week changes
- Note spikes and investigate causes
- Refine categorization criteria as needed

---

**STATUS:** Methodology complete. Collection plan ready. Tools identified.

**ESTIMATED INITIAL SCORE:** 20-26/100 (will refine with real data)

**START WITH:** Reddit + App Reviews (easiest, fastest, high signal)
