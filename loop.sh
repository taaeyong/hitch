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

Important execution rule:
- treat this invocation as exactly one implementation cycle
- do meaningful work for one coherent cycle
- if you make progress, commit and push it
- when the cycle is complete, exit cleanly instead of lingering in an idle TUI state
- do not remain attached waiting for a next instruction once the current cycle is done
PROMPT_EOF
)

exec codex --yolo "$PROMPT"
