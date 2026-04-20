#!/bin/bash
# Weekly Reddit collection, intended to be triggered by launchd on Monday mornings.
# Reddit blocks GitHub Actions IPs, so this runs on the owner's Mac instead.
#
# Flow:
#   1. Sync repo to origin/main
#   2. Run all 8 Reddit collectors + rescore + update metricDetailData.ts
#   3. Commit and push if anything changed
#
# Install the launchd job via scripts/install-launchd.sh.

set -u

REPO_DIR="$HOME/absurdity-index"
LOG_DIR="$HOME/Library/Logs"
LOG_FILE="$LOG_DIR/absurdity-index-weekly-reddit.log"

mkdir -p "$LOG_DIR"

log() {
  echo "[$(date +'%Y-%m-%d %H:%M:%S')] $*" >> "$LOG_FILE"
}

log "=== Weekly Reddit update starting ==="

if [ ! -d "$REPO_DIR/.git" ]; then
  log "FATAL: $REPO_DIR is not a git repo."
  exit 1
fi

cd "$REPO_DIR" || { log "FATAL: cd failed"; exit 1; }

# Ensure a clean tree before pulling. Abort if local changes exist —
# we don't want the automated job to clobber in-progress work.
if ! git diff --quiet || ! git diff --cached --quiet; then
  log "FATAL: working tree has uncommitted changes. Skipping to protect local work."
  exit 1
fi

log "Fetching latest from origin/main"
if ! git fetch origin main >> "$LOG_FILE" 2>&1; then
  log "FATAL: git fetch failed"
  exit 1
fi

if ! git pull --ff-only origin main >> "$LOG_FILE" 2>&1; then
  log "FATAL: git pull --ff-only failed (branch diverged?)"
  exit 1
fi

log "Running Reddit collectors + rescore + metricDetailData update"
cd data-collection || { log "FATAL: cd data-collection failed"; exit 1; }

if ! /usr/local/bin/python3 run_weekly_update.py --reddit-only >> "$LOG_FILE" 2>&1; then
  log "WARN: run_weekly_update.py exited non-zero (continuing to commit whatever was produced)"
fi

cd "$REPO_DIR" || exit 1

if git diff --quiet && git diff --cached --quiet; then
  log "No changes to commit. Done."
  exit 0
fi

log "Committing and pushing"
git add data-collection/collected-data/ lib/metricDetailData.ts 2>> "$LOG_FILE"

COMMIT_MSG="Weekly Reddit update - $(date +'%Y-%m-%d')

Automated collection from local Mac via launchd (Reddit blocks CI IPs).
Refreshed Reddit CSVs, recalculated scores, updated metricDetailData.ts."

if git diff --staged --quiet; then
  log "Nothing staged (ignored files only?). Done."
  exit 0
fi

if ! git commit -m "$COMMIT_MSG" >> "$LOG_FILE" 2>&1; then
  log "FATAL: git commit failed"
  exit 1
fi

if ! git push origin main >> "$LOG_FILE" 2>&1; then
  log "FATAL: git push failed"
  exit 1
fi

log "=== Weekly Reddit update complete ==="
