#!/bin/bash
set -euo pipefail
cd "$(dirname "$0")"

PROMPT=$(cat <<'PROMPT_EOF'
Continue advancing Hitch from the current repo state.
Read README.md, spec/, ops/, and the existing local code/artifacts first.
Do not stop at static analysis if meaningful implementation work remains.

Current operating goal:
- keep local development moving toward a runnable rehearsal path
- strengthen simulation -> wiki feedback -> graph artifact accumulation
- strengthen Telegram demo readiness
- fix blockers immediately when found
- revise code or shell scripts freely if that is the best path
- keep the work coherent and inspectable
- prefer meaningful forward motion over perfectionism
- keep private raw data and .env local-only
- commit in small coherent slices and push frequently when appropriate for this repo mode

Behave like an active implementation loop pursuing the goal, not a one-shot answerer.
PROMPT_EOF
)

exec codex --yolo "$PROMPT"
