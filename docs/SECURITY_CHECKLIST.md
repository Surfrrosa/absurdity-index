# Security Checklist

## Secrets Management

- [x] No secrets committed to version control
- [x] `.env` files gitignored (`.env*` pattern in `.gitignore`, `!.env.example` exempted)
- [x] API keys stored in GitHub Secrets for CI (`YOUTUBE_API_KEY`, `FRED_API_KEY`)
- [x] Root `.env.example` documents required variables without values
- [x] `data-collection/.env.example` documents required variables with setup instructions

## Data Security

- [x] Collected CSV data gitignored (`data-collection/*.csv`)
- [x] Collected JSON data gitignored (`data-collection/*.json`, except `config.json`)
- [x] No PII collected (social media data is public posts, no user identification)
- [x] API usage within free tier limits (YouTube 10K units/day, FRED unlimited)

## Web Security

- [x] HTTPS enforced (Vercel default)
- [x] No user input fields (static dashboard, no forms, no auth)
- [x] No backend API routes (all data baked at build time)
- [x] Fonts self-hosted via next/font (no external font requests at runtime)
- [x] Vercel Analytics loaded from first-party domain

N/A for this project: CORS, CSRF, cookies, rate limiting, session management, input sanitization (no backend, no forms, no auth).

## Dependencies

- [x] Node.js dependencies pinned to exact versions (no `^` or `~`)
- [x] Python requirements use `>=` minimum versions (acceptable for data collection scripts, not deployed)
- [ ] Regular `npm audit` checks (not automated yet)

## CI/CD Security

- [x] GitHub Actions uses pinned action versions
- [x] Secrets accessed via `${{ secrets.* }}` (not hardcoded)
- [x] Validation gate prevents empty data from corrupting scores
- [x] Build verification step before auto-commit

## Audit Log

| Date | Action | Result |
|------|--------|--------|
| 2026-02-19 | Pipeline hardened: empty-data guards, validation gate | Commit `02c37da` |
| 2026-02-19 | WCAG AA contrast fix (red-700 for backgrounds) | Commit `24dcd8e` |
| 2026-02-22 | Initial security checklist created, dependencies pinned | This update |
