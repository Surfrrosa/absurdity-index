# Architecture

The Absurdity Index is a data-driven dashboard quantifying modern absurdity through 8 metrics. It combines official government statistics (40% weight) with social media sentiment analysis (60% weight).

**Live site:** [absurdity-index.vercel.app](https://absurdity-index.vercel.app)

For visual design specs, see [DESIGN_SYSTEM.md](../DESIGN_SYSTEM.md).
For scoring formulas, see [data-collection/METHODOLOGY_FORMULAS.md](../data-collection/METHODOLOGY_FORMULAS.md).
For running collectors, see [data-collection/COLLECTION_QUICKSTART.md](../data-collection/COLLECTION_QUICKSTART.md).

## System Overview

```
                    Weekly (Mon 9AM UTC)
                    GitHub Actions CI
                          |
    +---------+-----------+-----------+---------+
    |         |           |           |         |
 YouTube   TikTok    Hacker News   CFPB      FRED
 (8 collectors)  (via YT)   (Algolia)   (complaints) (economic data)
    |         |           |           |         |
    +----+----+-----------+-----------+---------+
         |
    CSV files (gitignored)
         |
    calculate_all_social_scores.py
         |
    update_metric_data.py
         |
    lib/metricDetailData.ts  <-- single source of truth
         |
    Next.js frontend (Vercel auto-deploy)
```

## Frontend

**Stack:** Next.js 16 / React 19 / TypeScript / Tailwind CSS 4

### Routes

| Route | Page | Purpose |
|-------|------|---------|
| `/` | `app/page.tsx` | Dashboard: overall score + 8 metric cards |
| `/methodology` | `app/methodology/page.tsx` | Data transparency (dynamic from metricDetailData) |
| `/status` | `app/status/page.tsx` | Pipeline health monitoring |

### Component Hierarchy

```
app/page.tsx
├── Header.tsx              Nav with DATA / STATUS links
├── AbsurdityScore.tsx      Animated overall score + progress bar
├── MetricCard.tsx (x8)     Individual metric, 50% threshold flip
│   └── MetricDetail.tsx    Modal: samples, sources, level distribution
└── Footer
```

### State Management

Client-side `useState` only (selected metric for modal, animation state). No external state library. All metric data is statically imported from `lib/metricDetailData.ts` at build time.

### Key Modules

| File | Purpose |
|------|---------|
| `lib/metricDetailData.ts` | All 8 metrics: scores, samples, sources, trends. Auto-updated by CI weekly. |
| `lib/metricLabels.ts` | Dynamic labels per metric (5 severity thresholds each) |
| `app/globals.css` | Brutalist design system, animations, CSS variables |
| `app/layout.tsx` | Root layout, metadata, self-hosted fonts via next/font |

## Data Collection Pipeline

**7 platforms, 44 Python scripts, weekly automated collection.**

### Platforms

| Platform | Auth | Metrics Covered | Collector |
|----------|------|----------------|-----------|
| YouTube | API key | All 8 | 8 individual `*-youtube-collector.py` |
| TikTok | Via YouTube API | 3 of 8 | `tiktok-youtube-collector.py` |
| Hacker News | None (Algolia) | 5 of 8 | `hackernews-collector.py` |
| CFPB | None (public API) | 3 of 8 | `cfpb-collector.py` |
| FRED | API key | 4 of 8 | `fred-collector.py` |
| Reddit | OAuth | All 8 | 8 individual `*-reddit-collector.py` (local only, blocked in CI) |
| Bluesky | None (AT Protocol) | All 8 | `bluesky-collector.py` (currently 403) |

### Scoring Formula

```
Final Score = (Official Score x 0.4) + (Social Score x 0.6)

Social Score = sum(severity_weight x log10(engagement + 1)) / sum(log10(engagement + 1)) x 100

Severity weights: L1 (Aware) = 0.33, L2 (Struggling) = 0.67, L3 (Crisis) = 1.0
```

Log10 engagement weighting prevents viral outliers from dominating scores. Centralized in `data-collection/config.json`.

### Processing Pipeline

1. **Collect** — Run all collectors, output timestamped CSVs
2. **Validate** — CI gate: skip downstream if no files > 200 bytes created
3. **Deduplicate** — `deduplicate_reddit_posts.py` removes cross-metric dupes
4. **Score** — `calculate_all_social_scores.py` computes social scores from all platforms
5. **Update** — `update_metric_data.py` rewrites `lib/metricDetailData.ts` with new scores, samples, trends
6. **Build** — `npm run build` verifies TypeScript compilation
7. **Commit & Push** — Auto-commit to main, Vercel auto-deploys

### Configuration

`data-collection/config.json` is the single source of truth for:
- Formula weights (official: 0.4, social: 0.6)
- Severity weights (L1, L2, L3)
- Per-metric definitions: name, slug, official_score, collection_targets

## CI/CD

**Workflow:** `.github/workflows/weekly-data-update.yml`
**Schedule:** Every Monday 9:00 AM UTC
**Trigger:** Cron + manual dispatch

Steps: checkout → setup Python 3.11 → install requirements → run collectors → validation gate → deduplicate → score → update TS → build → commit → push

## Environment Variables

| Variable | Required By | Where Stored |
|----------|-------------|-------------|
| `YOUTUBE_API_KEY` | YouTube + TikTok collectors | `.env` (local), GitHub Secrets (CI) |
| `FRED_API_KEY` | FRED collector | `.env` (local), GitHub Secrets (CI) |

See `.env.example` for setup instructions.
