#!/bin/bash
set -euo pipefail
cd "$(dirname "$0")"

MAX_CYCLES="${MAX_CYCLES:-0}"
SLEEP_SECONDS="${SLEEP_SECONDS:-10}"
CYCLE=0

while true; do
  CYCLE=$((CYCLE + 1))
  echo "[controller] starting cycle ${CYCLE} at $(date '+%Y-%m-%d %H:%M:%S %Z')"

  if ! bash ./loop.sh; then
    echo "[controller] loop cycle ${CYCLE} failed at $(date '+%Y-%m-%d %H:%M:%S %Z')"
  else
    echo "[controller] loop cycle ${CYCLE} completed at $(date '+%Y-%m-%d %H:%M:%S %Z')"
  fi

  git status --short || true
  git log --oneline -n 3 || true

  if [ "$MAX_CYCLES" != "0" ] && [ "$CYCLE" -ge "$MAX_CYCLES" ]; then
    echo "[controller] reached MAX_CYCLES=${MAX_CYCLES}, exiting"
    break
  fi

  echo "[controller] sleeping ${SLEEP_SECONDS}s before next cycle"
  sleep "$SLEEP_SECONDS"
done
