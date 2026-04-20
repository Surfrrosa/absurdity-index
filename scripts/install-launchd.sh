#!/bin/bash
# Install (or reinstall) the weekly Reddit launchd job.
#
# Fires every Monday at 9:00 AM local time. If the Mac is asleep at
# that moment, the job is skipped for that week; the freshness gate
# in the GitHub weekly workflow will flag stale Reddit data via a
# GitHub issue, and you can run scripts/weekly-reddit.sh manually.

set -e

LABEL="com.surfrrosa.absurdity-index.weekly-reddit"
PLIST="$HOME/Library/LaunchAgents/${LABEL}.plist"
SCRIPT="$HOME/absurdity-index/scripts/weekly-reddit.sh"
LOG_DIR="$HOME/Library/Logs"

if [ ! -x "$SCRIPT" ]; then
  chmod +x "$SCRIPT"
fi

mkdir -p "$LOG_DIR"

cat > "$PLIST" <<EOF
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>Label</key>
    <string>${LABEL}</string>

    <key>ProgramArguments</key>
    <array>
        <string>/bin/bash</string>
        <string>${SCRIPT}</string>
    </array>

    <key>StartCalendarInterval</key>
    <dict>
        <key>Weekday</key>
        <integer>1</integer>
        <key>Hour</key>
        <integer>9</integer>
        <key>Minute</key>
        <integer>0</integer>
    </dict>

    <key>RunAtLoad</key>
    <false/>

    <key>AbandonProcessGroup</key>
    <true/>

    <key>StandardOutPath</key>
    <string>${LOG_DIR}/absurdity-index-weekly-reddit.stdout.log</string>

    <key>StandardErrorPath</key>
    <string>${LOG_DIR}/absurdity-index-weekly-reddit.stderr.log</string>

    <key>EnvironmentVariables</key>
    <dict>
        <key>PATH</key>
        <string>/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin</string>
        <key>HOME</key>
        <string>${HOME}</string>
    </dict>
</dict>
</plist>
EOF

# Unload if already loaded (ignore errors on fresh install)
launchctl unload "$PLIST" 2>/dev/null || true

launchctl load "$PLIST"

echo "Installed: $PLIST"
echo "Next fire: Monday 9:00 AM local time"
echo "Logs:     $LOG_DIR/absurdity-index-weekly-reddit.log"
echo ""
echo "Manual trigger:  bash $SCRIPT"
echo "Check status:    launchctl list | grep ${LABEL}"
echo "Uninstall:       launchctl unload $PLIST && rm $PLIST"
