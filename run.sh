#!/bin/bash
set -euo pipefail
cd "$(dirname "$0")"

PROMPT=$(cat <<'PROMPT_EOF'
Read README.md, spec/, ops/, especially spec/demo-run.md and spec/simulation-run.md.
Your job is to move Hitch toward the current goal instead of blindly following a fixed scaffold.
Think flexibly about the best way to achieve the product goal.

Current goal:
- make local runnable rehearsal progress from the current repo state
- create or repair the runnable code path when missing
- keep Telegram demo and simulation loop both in view
- keep girlfriend-data-grounded wiki/simulation/graph accumulation in view
- prefer coherent progress over rigid script obedience
- if code or shell scripts need to change, change them
- if repo structure needs adjustment to achieve the goal, adjust it
- keep private raw data and .env local-only
- commit in small coherent slices and push frequently when appropriate for this repo mode

Use the highest available reasoning effort and act like an implementation partner, not a passive transpiler.
PROMPT_EOF
)

exec codex --yolo "$PROMPT"
