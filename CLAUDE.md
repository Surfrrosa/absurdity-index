# Claude Code Instructions for The Absurdity Index

## Before Starting Any Work

**Read the latest session log first.**

Session logs are in `docs/sessions/` with format `YYYY-MM-DD_session.md`.

Then read it to understand:
- What was accomplished
- Current state of the project
- Next tasks already identified
- Known issues and blockers

This prevents duplicate work and ensures continuity.

---

## Project Overview

The Absurdity Index is a data-driven dashboard quantifying the absurdity of modern existence through 8 metrics combining official statistics with social media sentiment analysis.

**Stack:** Next.js 16, React 19, TypeScript, Tailwind CSS 4, Python 3 data collection, Vercel hosting, GitHub Actions CI

**Scoring formula:** `Final Score = (Official Data x 0.4) + (Social Sentiment x 0.6)`

**Social score:** Engagement-weighted severity using `log10(views+1)` and 3-level categorization (L1=0.33, L2=0.67, L3=1.0)

**Overall score:** Equal-weight average of all 8 metric final scores

---

## Key Files

### Frontend
| File | Purpose |
|------|---------|
| `app/page.tsx` | Main dashboard page |
| `app/methodology/page.tsx` | Dynamic methodology page (pulls from metricDetailData) |
| `app/status/page.tsx` | Pipeline health status page |
| `app/layout.tsx` | Root layout with next/font imports |
| `app/globals.css` | Global styles, font variables, animations |
| `components/MetricCard.tsx` | Individual metric card with crisis flip at 50+ |
| `components/MetricDetail.tsx` | Modal with full metric details, focus trap |
| `components/AbsurdityScore.tsx` | Animated overall score display |
| `components/Header.tsx` | Nav header with DATA and STATUS links |
| `lib/metricDetailData.ts` | All metric scores, samples, sources (auto-updated by CI) |
| `lib/metricLabels.ts` | Dynamic labels per metric based on score thresholds |

### Data Collection (Python)
| File | Purpose |
|------|---------|
| `data-collection/*-youtube-collector.py` | 8 YouTube collectors (one per metric) |
| `data-collection/*-reddit-collector.py` | 8 Reddit collectors (blocked in CI, local only) |
| `data-collection/tiktok-youtube-collector.py` | TikTok via YouTube compilations |
| `data-collection/content_filters.py` | Clickbait/spam filter for YouTube |
| `data-collection/calculate_all_social_scores.py` | Score calculator (skips files < 5 rows) |
| `data-collection/update_metric_data.py` | Updates metricDetailData.ts with computed scores + trend |
| `data-collection/deduplicate_reddit_posts.py` | Cross-metric Reddit deduplication |
| `data-collection/requirements.txt` | Python dependencies |
| `data-collection/.env.example` | Environment variable template |

### CI/CD
| File | Purpose |
|------|---------|
| `.github/workflows/weekly-data-update.yml` | Weekly Monday 9AM UTC: collect, score, update TS, build, commit |

---

## Design System

- **Aesthetic:** Brutalist. No rounded corners, no gradients.
- **Palette:** Black, white, red-700 (bg with white text), red-600 (text on dark bg, decorative)
- **No emojis** anywhere in the codebase or customer-facing content
- **50% threshold rule:** Metric cards flip to crisis mode (red bg, white text) at score >= 50
- **Fonts:** Archivo Black (headings), Space Grotesk (body), Roboto Mono (data) -- loaded via next/font

---

## Data Collection Rules

- All collectors have empty-data guards. If 0 results are collected, the CSV file is NOT written. This preserves previous good data.
- The score calculator (`calculate_all_social_scores.py`) skips CSV files with fewer than 5 data rows.
- The CI workflow has a validation gate: if no new data is collected, it skips score recalculation and commit.
- Reddit collectors are blocked from GitHub Actions IPs. They only work locally.
- `update_metric_data.py` calculates trend by comparing old vs new scores (2-point threshold).

---

## Running Locally

```bash
# Frontend
npm run dev

# Data collection (requires YOUTUBE_API_KEY in .env)
cd data-collection
pip install -r requirements.txt
python healthcare-youtube-collector.py  # example

# Score calculation
python calculate_all_social_scores.py

# Update TypeScript data file
python update_metric_data.py

# Build check
npm run build
```

---

## Session Log Format

When ending a session, create `docs/sessions/YYYY-MM-DD_session.md` with:
1. Date and status
2. What was accomplished
3. Next tasks (prioritized)
4. Any blockers
5. Key decisions made
6. Known issues discovered

Update `docs/sessions/README.md` with a one-line summary in the sessions table.
