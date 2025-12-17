# Data Collection Quick Start Guide

## Step-by-Step: Collecting Your First Healthcare Data

### 1. Find Content on Reddit (Easiest to start)

**Go to:** https://reddit.com/r/HealthInsurance

**Sort by:** Top posts from Past Month

**Look for posts about:**
- Insurance denied my claim
- Prior authorization nightmares
- Can't afford healthcare
- Medical debt
- Premium increases

**What to collect:**
- Post title
- First 200-300 characters of content
- Full Reddit URL (e.g., https://reddit.com/r/HealthInsurance/comments/abc123)
- Post date
- Note if it's Level 1/2/3 based on severity

---

### 2. Add Data to Script

Open `healthcare-collector.py` and scroll to the bottom. Add entries like this:

```python
# Initialize collector
collector = HealthcareDataCollector()

# Example Entry 1 - Level 3 (Crisis)
entry = HealthcareEntry(
    platform="reddit",
    content_id="1h9xy2z",  # From URL
    title="Insurance denied my cancer treatment",
    content="After paying premiums for 10 years, my insurance denied coverage for my oncologist-recommended treatment. Now facing bankruptcy while fighting the appeal. They said it wasn't 'medically necessary' despite doctor's orders.",
    url="https://reddit.com/r/HealthInsurance/comments/1h9xy2z",
    date="2025-12-10"
)
collector.add_entry(entry)

# Example Entry 2 - Level 2 (Struggling)
entry = HealthcareEntry(
    platform="reddit",
    content_id="1h8abc3",
    title="Premium went up 15% this year",
    content="My family plan went from $720/month to $828/month. That's almost $1,300 more per year for the same coverage. Meanwhile my deductible also went up.",
    url="https://reddit.com/r/HealthInsurance/comments/1h8abc3",
    date="2025-12-08"
)
collector.add_entry(entry)

# When you have 20-30 entries, export
print(collector.get_stats())
collector.export_json("healthcare_data.json")
```

---

### 3. Run the Script

```bash
cd "/Volumes/Extreme SSD/Home/projects/disappointments-dashboard-web/data-collection"
python3 healthcare-collector.py
```

This will create `healthcare_data.json` with your collected data + calculated scores.

---

### 4. Load Data Into Dashboard

The JSON file will look like this:

```json
{
  "metadata": {
    "collected_at": "2025-12-16T22:30:00",
    "metric": "What Healthcare?",
    "stats": {
      "total": 30,
      "level_1": 8,
      "level_2": 12,
      "level_3": 10,
      "crisis_ratio": 33.3,
      "official_score": 36.17,
      "final_score": 64.47
    }
  },
  "entries": [...]
}
```

Copy the `entries` array and `stats` object into `/lib/metricDetailData.ts` to update the dashboard.

---

## Pro Tips

### Categorization Guide

**Level 3 (Crisis):**
- Medical debt/bankruptcy
- Denied life-saving treatment
- Can't afford necessary medication
- Lost coverage during emergency
- Financial ruin from medical bills

**Level 2 (Struggling):**
- Can't afford treatment (non-emergency)
- High premiums causing budget strain
- Prior authorization battles
- Fighting denials
- Coverage gaps

**Level 1 (Mild):**
- Billing confusion
- Administrative frustrations
- Minor delays
- General complaints

### Efficiency Tips

1. **Batch collect**: Get 20-30 URLs at once, then add them all to script
2. **Use Reddit search**: Search "denied claim" in r/HealthInsurance, sort by Top (Past Month)
3. **Copy content ID from URL**: `reddit.com/r/sub/comments/abc123` → content_id is "abc123"
4. **Don't overthink categorization**: The keywords auto-categorize, just verify it makes sense
5. **Start with Reddit**: Easier than YouTube (no transcripts needed)

### Quality Control

- Every entry MUST have real, verifiable URL
- Content should be direct quotes (first 200-300 chars of post)
- Dates should be actual post dates
- Platform must be lowercase ("reddit", "youtube", "tiktok")

---

## Target Goals

### Initial Batch (Proof of Concept)
- 30-50 entries
- Mix of platforms (mostly Reddit to start)
- At least 10 Level 3 entries

### Full Collection
- 440-480 total entries
- YouTube: 120-160 videos
- Reddit: 200 posts
- TikTok: 120 videos

---

## Next Steps After First Batch

1. Run script, verify JSON export works
2. Check that crisis ratio calculation makes sense
3. Load data into dashboard
4. Click "What Healthcare?" card to see real stories
5. Validate the entire pipeline works end-to-end
6. Then scale up to full 440-480 collection

---

## Troubleshooting

**Script won't run:**
```bash
chmod +x healthcare-collector.py
python3 healthcare-collector.py
```

**JSON export fails:**
- Check that all entries have all required fields
- Make sure content_id, title, content, url, date, platform are all strings

**Categorization seems wrong:**
- You can manually override by setting `entry.level = 3` before adding

**Need help:**
- Check the categorization keywords in the script
- Verify URLs are correct format
- Make sure dates are in YYYY-MM-DD format
