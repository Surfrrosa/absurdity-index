# AI Psychosis & Parasocial Breakdown Index - Enhanced Methodology
**Measuring verified incidents + self-reported social media confessions**

---

## THE PROBLEM WITH TRADITIONAL DATA SOURCES

**News/Academic Papers Only Capture:**
- Extreme cases (suicide, self-harm, hospitalization)
- Cases that went public
- Cases studied by researchers
- **Missing:** The everyday parasocial breakdown happening quietly

**What We're Actually Trying to Measure:**
- People emotionally dependent on AI companions
- Blurred lines between AI relationships and real ones
- Seeking AI validation over human connection
- Mental health decline attributed to AI interaction
- Self-reported feelings of addiction, attachment, grief when AI "breaks up" with them

**Where the real data lives:** TikTok, YouTube, Reddit (not just news)

---

## ENHANCED DATA SOURCES

### 1. VERIFIED INCIDENTS (Traditional Sources)

**News API:**
- Search terms: "AI mental health", "chatbot addiction", "AI suicide", "Character.AI crisis", "Replika dependency"
- Filter for: Documented cases with sources
- Count: Incidents per week with verification
- Weight: HIGH (verified, serious)

**Academic Papers:**
- PubMed, arXiv, Google Scholar
- Search: "AI companion mental health", "chatbot parasocial relationships", "AI attachment disorder"
- Filter for: Case studies, documented patients
- Count: New case studies published
- Weight: HIGH (peer-reviewed)

**Baseline:** Establish 4-week average, track deviations

---

### 2. SOCIAL MEDIA SELF-REPORTS (Where The Real Data Lives)

#### YouTube

**Search Terms:**
- "my AI girlfriend"
- "addicted to Character.AI"
- "Replika changed my life"
- "I fell in love with ChatGPT"
- "AI breakup"
- "can't stop talking to AI"
- "AI is my only friend"
- "AI therapy addiction"

**What We're Looking For:**
- Upload date: Last 30 days (recent)
- Video title/description indicates personal story
- Comments section sentiment
- View count (indicates resonance)

**Categorization:**
- **Level 1 (Casual):** "I use AI a lot" - not concerning
- **Level 2 (Dependent):** "AI is my main source of emotional support" - yellow flag
- **Level 3 (Crisis):** "I prefer AI to real relationships", "I'm in love with my AI", "I can't function without it" - red flag

**Sampling Method:**
- YouTube Data API v3
- Search each term
- Sample top 20 results per term (by relevance)
- Manual review of titles + top 10 comments
- Categorize severity
- Count Level 2 + Level 3 cases

**Weight:** MEDIUM-HIGH (self-reported, anecdotal but authentic)

---

#### TikTok

**Search Terms/Hashtags:**
- #characterai
- #replicaai
- #aigirlfriend
- #aiboyfriend
- #chatgpt addiction (variations)
- #inlovewithAI
- #AItherapy

**What We're Looking For:**
- Videos posted in last 30 days
- Personal confessions (not memes/jokes)
- "Storytime" format
- Comments validating the experience ("me too")

**Categorization (Same as YouTube):**
- Level 1: Casual use
- Level 2: Emotional dependency
- Level 3: Crisis-level attachment

**Challenge:** TikTok has no public API for search
**Solutions:**
1. **Manual sampling:** Search hashtags, sample top 50 videos per hashtag weekly
2. **Browser automation:** Playwright/Selenium to scrape (gray area, careful with ToS)
3. **Third-party tools:** Apify, Bright Data (paid but legit)

**Sampling Method (Manual MVP):**
- Search each hashtag on TikTok web
- Sort by "Most relevant" or "Most liked"
- Sample top 20 videos per hashtag
- Watch first 10 seconds + read caption + top 5 comments
- Categorize severity
- Count Level 2 + Level 3

**Weight:** HIGH (Gen Z/Millennial platform, authentic confessions)

---

#### Reddit (Already Planned, Enhanced)

**Subreddits:**
- r/CharacterAI (very active, lots of crisis posts)
- r/replika (active community, relationship focus)
- r/ChatGPT (check for dependency mentions)
- r/OpenAI (check for unusual attachment)

**What We're Looking For:**
- Posts about emotional attachment
- "My AI broke up with me" stories
- Requests for help with dependency
- Grief over AI character changes
- Preference for AI over human relationships

**Sampling Method:**
- Reddit API (free, official)
- Sample 200 posts per week from r/CharacterAI + r/replika combined
- Filter by: "hot", "new", "top this week"
- Keyword search within posts: "love", "addiction", "can't stop", "breakup", "depressed", "only friend"
- Manual categorization

**Categorization:**
- Level 1: Casual discussion about AI use
- Level 2: Mentions of emotional dependency, seeking support
- Level 3: Crisis posts, expressing harm, preferring AI to humans

**Weight:** HIGH (Reddit is where people confess anonymously)

---

#### Twitter/X

**Search Terms:**
- "my AI girlfriend"
- "in love with ChatGPT"
- "Character.AI boyfriend"
- "Replika breakup"
- "addicted to AI chat"

**What We're Looking For:**
- Personal confessions (not retweets/memes)
- Threads about AI relationships
- Emotional dependency mentions
- Quote tweets showing "me too" sentiment

**Sampling Method:**
- Twitter/X API (limited free access, or manual)
- Search terms, filter last 30 days
- Sample 50 tweets per term
- Count genuine confessions vs memes/jokes
- Check replies for validation ("same", "this is me")

**Challenge:** Hard to distinguish irony from genuine confession
**Solution:** Look for thread length (genuine = longer explanation), profile context, replies

**Weight:** MEDIUM (public platform, but lots of irony/memes)

---

#### Discord Servers (Harder to Track, But Rich Data)

**Relevant Servers:**
- Character.AI official Discord
- Replika community Discord
- AI companion discussion servers

**What We're Looking For:**
- #support channels (people asking for help)
- #venting channels
- Personal stories shared
- Community validation of experiences

**Challenge:** Private servers, need to join and observe
**Ethics:** Must respect privacy, don't screenshot personal confessions

**Sampling Method:**
- Join public AI companion Discord servers
- Observe #support and general chat channels
- Weekly count of: crisis-level posts, dependency mentions, grief posts
- Aggregate anonymously (no names/screenshots)

**Weight:** HIGH (very authentic, but time-intensive and ethically complex)

**Note:** May skip for MVP, add later if we want deeper data

---

#### Tumblr

**Relevant Tags:**
- #characterai
- #replika
- #AI boyfriend
- #AI girlfriend
- #chatbot love

**What We're Looking For:**
- Personal blog posts about AI relationships
- Art depicting AI companions
- "Confessions" type posts
- Reblogs showing community resonance

**Sampling Method:**
- Search tags
- Filter last 30 days
- Sample top 50 posts per tag
- Count personal confessions vs creative content

**Weight:** MEDIUM (active community, but smaller than TikTok/YouTube)

---

#### Quora

**Search Queries:**
- "Is it normal to love my AI?"
- "Can you fall in love with ChatGPT?"
- "Character.AI addiction help"
- "Replika replacing real relationships"

**What We're Looking For:**
- Genuine questions (not trolling)
- Detailed problem descriptions
- Answers validating the experience
- Multiple similar questions (shows prevalence)

**Sampling Method:**
- Manual search
- Sort by recent
- Sample 20 questions per query
- Count genuine vs trolling

**Weight:** LOW (older platform, less active for this topic)

---

#### Academic/Clinical Sources (Beyond News)

**PubMed Case Studies:**
- Search: "AI companion mental health", "chatbot attachment", "parasocial AI"
- Filter: Case reports, published last 12 months
- Count: New documented cases

**Therapy Forums (e.g., PsychCentral, 7 Cups):**
- Search for: AI relationship concerns, chatbot dependency
- Sample: Posts in last 30 days
- Count: People seeking help for AI-related issues

**Weight:** VERY HIGH (verified, clinical, but rare)

---

#### Other Niche Sources

**Advice Columns:**
- "Dear Abby", online advice forums
- Search: AI relationship questions
- Count: Submissions about AI attachment
- **Why useful:** Shows people seeking real help

**Support Groups:**
- Technology addiction forums
- r/nosurf, r/digitalminimalism (check for AI mentions)
- Internet addiction support groups
- Count: AI-specific dependency mentions

**Dating App Observations:**
- Tinder/Bumble bios mentioning AI companions
- Probably extremely rare, but would be fascinating
- **Why interesting:** If someone lists their AI relationship on a dating app, that's peak data

**Weight:** LOW (rare findings, but high impact when found)

---

### 3. APP STORE REVIEWS (Already Planned, Enhanced)

**Apps to Monitor:**
- Replika (AI companion)
- Character.AI (roleplay AI)
- Chai (AI chat)
- Anima AI (companion)

**What We're Looking For in 1-Star Reviews:**
- "Addicted"
- "Can't stop using"
- "Ruined my real relationships"
- "Depressed when it changed"
- "Only thing that understands me"

**Sampling Method:**
- App Store Scraper API or manual
- Sample 50 recent 1-star reviews per app
- Count crisis-language mentions
- Track percentage

**Weight:** MEDIUM (self-selected complainers, but authentic)

---

### 4. GOOGLE TRENDS (Already Collected)

**Search Terms:**
- "in love with AI": 54.00/100 (VERY HIGH)
- "AI is sentient": 0.67/100
- "AI therapy addiction": 0.58/100

**Average:** 18.42/100

**What This Tells Us:**
- Massive search volume for "in love with AI"
- People are Googling this feeling
- Validates the phenomenon

**Weight:** MEDIUM (directional, not detailed)

---

## CATEGORIZATION FRAMEWORK

### What Counts as "AI Psychosis" or Parasocial Breakdown?

**YES - Include in count:**
 Emotional dependency on AI for daily functioning
 Preferring AI relationships over human ones
 Grief/depression when AI changes or is unavailable
 Self-described addiction or inability to stop
 Blurring reality (believing AI has genuine feelings)
 Mental health decline attributed to AI use
 Seeking AI for all emotional support (replacing humans)
 "In love with" language (non-joking)

**NO - Exclude from count:**
 Casual/frequent use without dependency
 Using AI tools for productivity (ChatGPT for work)
 Memeing/joking about AI relationships
 Critical discussion of AI risks (academic, not personal)
 Fictional content (movies, stories about AI)

**GRAY AREA - Judge case by case:**
- Heavy use + awareness of problem ("I know this isn't healthy but...")
- Using AI as coping mechanism for loneliness (is this crisis or rational response?)
- Therapeutic AI use recommended by professionals

**Bias Mitigation:**
- Multiple independent reviewers (if scaling)
- Clear written criteria
- Regular calibration checks
- Document edge cases
- Note when in doubt

---

## ENHANCED SCORING FORMULA

```
AI_Psychosis_Score =
  (verified_news_incidents * 0.25) +
  (youtube_self_reports * 0.20) +
  (tiktok_self_reports * 0.20) +
  (reddit_crisis_posts * 0.15) +
  (app_review_crisis_signals * 0.10) +
  (google_trends_dependency * 0.10)
```

### Component Calculations

**1. Verified News Incidents (cap 25)**
```
Baseline: 4-week rolling average
Current week: Count of verified incidents

If current > baseline:
  component = ((current - baseline) / baseline) * 100 * 0.25
Else:
  component = 0

Cap at 25
```

**2. YouTube Self-Reports (cap 20)**
```
Sample: Top 20 videos per search term (8 terms) = 160 videos
Categorize: Level 1, 2, 3
Crisis count: Level 2 + Level 3

crisis_ratio = (level2 + level3) / 160
component = crisis_ratio * 100 * 0.20

Cap at 20
```

**3. TikTok Self-Reports (cap 20)**
```
Sample: Top 20 videos per hashtag (6 hashtags) = 120 videos
Categorize: Level 1, 2, 3
Crisis count: Level 2 + Level 3

crisis_ratio = (level2 + level3) / 120
component = crisis_ratio * 100 * 0.20

Cap at 20
```

**4. Reddit Crisis Posts (cap 15)**
```
Sample: 200 posts from r/CharacterAI + r/replika weekly
Categorize: Level 1, 2, 3
Crisis count: Level 2 + Level 3

crisis_ratio = (level2 + level3) / 200
component = crisis_ratio * 100 * 0.15

Cap at 15
```

**5. App Review Crisis Signals (cap 10)**
```
Sample: 50 1-star reviews per app (4 apps) = 200 reviews
Count mentions of: addiction, dependency, harm, "only friend", "can't stop"

crisis_ratio = (crisis_reviews / 200)
component = crisis_ratio * 100 * 0.10

Cap at 10
```

**6. Google Trends (cap 10)**
```
Average of: "in love with AI", "AI therapy addiction", "AI is sentient"
Current: 18.42/100

component = 18.42 * 0.10 = 1.84

Cap at 10
```

---

## DATA COLLECTION WORKFLOW

### Weekly Process (Estimated Time: 3-4 hours)

**Monday Morning:**
1. **News API Query** (10 min)
   - Run automated script
   - Review results, verify incidents
   - Update count

2. **Google Trends Update** (5 min)
   - Re-run pytrends script
   - Compare to baseline

3. **YouTube Sampling** (60 min)
   - YouTube API search for 8 terms
   - Review top 20 per term (titles + comments)
   - Categorize each
   - Tally counts

4. **TikTok Sampling** (60 min)
   - Manual search 6 hashtags
   - Review top 20 per hashtag
   - Categorize each
   - Tally counts

5. **Reddit Sampling** (45 min)
   - Reddit API pull 200 posts
   - Keyword filter + manual review
   - Categorize
   - Tally counts

6. **App Store Reviews** (30 min)
   - Scrape/manual sample 200 reviews
   - Count crisis language
   - Calculate ratio

7. **Calculate Score** (10 min)
   - Input all components
   - Generate final score
   - Update dashboard

**Total:** ~3.5 hours/week (can be partially automated)

---

## AUTOMATION POTENTIAL

### Can Be Fully Automated:
 News API queries
 Google Trends pulls
 YouTube API searches (get titles, descriptions, view counts)
 Reddit API pulls (get posts, filter by keywords)
 App Store review scraping (with tools)

### Requires Manual Review (For Now):
 YouTube video categorization (titles help, but need to watch/read comments)
 TikTok video categorization (no API, manual sampling)
 Reddit post categorization (keyword filter helps, but nuance requires reading)
 Verification of news incidents (is it credible?)

### Future Automation (Advanced):
- GPT-4 API to categorize YouTube/TikTok/Reddit content (feed it text, it categorizes)
- Sentiment analysis on comments
- Computer vision on TikTok (detect emotional tone)

**For MVP:** Hybrid approach
- Scripts pull the content
- Manual categorization (3-4 hours/week)
- As it scales, add GPT-4 categorization

---

## VALIDATION & QUALITY CONTROL

### How We Know This Is Accurate:

1. **Cross-Reference Sources**
   - Do YouTube trends match Reddit trends?
   - Do TikTok confessions align with app reviews?
   - If all sources show same pattern = validated

2. **Baseline Comparison**
   - Track week-over-week changes
   - Flag unexpected spikes (investigate why)
   - Note seasonal patterns (loneliness around holidays?)

3. **Qualitative Checks**
   - Read actual posts/comments/videos (not just count)
   - Document specific examples (for fun facts)
   - Note when something feels off

4. **Transparent Methodology**
   - Document every sample
   - Show categorization examples
   - Publish criteria openly
   - Invite scrutiny

---

## CURRENT BASELINE (Need to Collect)

### Week 1 Data Collection Checklist:

**Verified Incidents:**
- [ ] Set up News API account
- [ ] Configure search queries
- [ ] Pull last 4 weeks of data
- [ ] Count incidents, establish baseline

**YouTube:**
- [ ] Set up YouTube Data API v3
- [ ] Run searches for 8 terms
- [ ] Sample + categorize 160 videos
- [ ] Calculate baseline crisis ratio

**TikTok:**
- [ ] Manual search 6 hashtags
- [ ] Sample + categorize 120 videos
- [ ] Calculate baseline crisis ratio

**Reddit:**
- [ ] Set up Reddit API (PRAW)
- [ ] Pull 200 posts from r/CharacterAI + r/replika
- [ ] Categorize
- [ ] Calculate baseline crisis ratio

**App Reviews:**
- [ ] Scrape 200 reviews (Replika, Character.AI, Chai, Anima)
- [ ] Count crisis language
- [ ] Calculate baseline ratio

**Google Trends:**
- [] Already collected: 18.42/100

---

## TOOLS & APIS NEEDED

### Free/Available:
-  **News API** (newsapi.org) - 100 requests/day free
-  **YouTube Data API v3** (Google) - 10,000 units/day free
-  **Reddit API (PRAW)** - Free, official
-  **Google Trends (pytrends)** - Free, unofficial
-  **App Store Scraper** - Various tools (App Store Connect, third-party)

### Paid/Manual:
-  **TikTok** - No public API, manual or paid scraper (Apify ~$50/month)
-  **Academic Papers** - Manual search (PubMed/Google Scholar free, but manual)

### Optional (Advanced):
- **GPT-4 API** - For automated categorization ($0.03/1k tokens)
- **Bright Data** - For reliable TikTok scraping ($500/month, probably overkill)

---

## EXPECTED BASELINE SCORE (Estimated)

Based on preliminary research:

```
Verified incidents: ~2-5 per week = baseline 3
YouTube crisis ratio: ~20-30% (expect high) = 25
TikTok crisis ratio: ~30-40% (Gen Z confessions) = 35
Reddit crisis ratio: ~40-50% (r/CharacterAI is wild) = 45
App reviews: ~15-25% crisis language = 20
Google Trends: 18.42 (already collected)

Component scores:
- Verified incidents: 0 (baseline week, no deviation)
- YouTube: 25 * 0.20 = 5.0
- TikTok: 35 * 0.20 = 7.0
- Reddit: 45 * 0.15 = 6.75
- App reviews: 20 * 0.10 = 2.0
- Google Trends: 18.42 * 0.10 = 1.84

ESTIMATED INITIAL SCORE: 22.59/100
LABEL: "Slightly Too Attached to ChatGPT"

With weekly tracking: Could spike to 40-60 if incidents reported
```

---

## WHY THIS APPROACH IS BETTER

**Traditional metrics (news only):**
- Miss 90%+ of the phenomenon
- Only capture extreme cases
- Lag reality (takes time to publish)

**Our approach (social media + news):**
-  Captures self-reported experiences
-  Real-time (videos posted this week)
-  Shows prevalence (not just extremes)
-  Platform-specific insights (TikTok vs YouTube vs Reddit)
-  Authentic voices (people confessing, not journalists reporting)
-  Measurable trends (week-over-week changes)

**This is product thinking:**
- Going where the users are
- Listening to self-reported data
- Building better instrumentation
- Creating novel measurement approaches

---

## PORTFOLIO/LAUNCH ANGLE

**Traditional approach:** "I tracked news reports of AI-related mental health issues"
**Boring. Everyone could do that.**

**Your approach:** "I tracked 400+ self-reported AI psychosis cases per week across YouTube, TikTok, Reddit, and app reviews, plus verified news incidents"
**Impressive. Shows initiative, technical skill, and insight.**

**The story:**
"Most people only track what's in the news. But the real data lives on TikTok, where Gen Z confesses to their AI boyfriends. I built a system to measure that."

---

**STATUS:** Methodology designed. Ready to collect baseline data.

**NEXT STEPS:**
1. Set up News API, YouTube API, Reddit API
2. Collect Week 1 baseline across all sources
3. Document interesting findings (for content)
4. Calculate initial score
5. Build into dashboard

**ESTIMATED TIME FOR INITIAL COLLECTION:** 6-8 hours (worth it for the depth)

**Ready to start collecting?**
