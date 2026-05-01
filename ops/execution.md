# Execution

## Purpose
This document describes the intended execution surfaces for Hitch v4 during development, operator use, and demo preparation.

## Main Execution Contexts
1. local repo development in `hitch-test-v4`
2. vanilla `codex`-driven implementation iterations
3. Telegram-facing runtime on Mac mini
4. raw txt/csv ingest jobs
5. wiki/simulation/report generation tasks
6. demo-safe artifact generation

## Execution Philosophy
- start simple
- prefer explicit commands over hidden automation during early iterations
- keep product/runtime/data boundaries legible
- do not over-automate before the domain model is stable

## Expected Iteration 2 Execution Paths
### 0. Implementation Entry
Preferred implementation entrypoint:
```bash
cd /Users/taaeyong/projects/hitch-test-v4
codex --yolo "Implement Hitch v4 using the current spec/ and ops/ docs. Build in small coherent slices, commit and push each safe slice promptly, and leave the repo runnable as a Telegram-first demo."
```

Practical mode guidance:
- default implementation path: vanilla `codex`
- preferred aggressive mode: `--yolo` (madmax equivalent)
- preferred reasoning posture: high, equivalent in spirit to earlier xhigh usage
- use `omx ralph` only as a fallback when direct Codex execution is not suitable

### 1. Repo / Spec Work
- read `spec/README.md`
- follow `spec/demo-run.md` and `spec/simulation-run.md`
- extend the scaffold into a minimally real relationship-system core

### 2. Raw Ingest Work
- accept txt drops under `raw/kakao/...`
- load and register source files
- produce parse-ready or parse-placeholder outputs under `data/`

### 3. Relationship Space Work
- create or update relationship-space metadata
- persist minimum creation set
- expose a stable path for future daily/weekly flow state

### 4. Simulation / Wiki Work
- create simulation run records
- persist wiki-oriented structured outputs
- generate visible evolution in local data layers

### 5. Demo Work
- preserve the Telegram-first story
- surface visible wiki growth
- expose only sanitized demo-safe pushable artifacts

### 6. Current Core Verification
The current runnable demo is pure Python with no new runtime dependencies. Use:
```bash
python3 -m unittest discover -s tests
PYTHONPYCACHEPREFIX=/tmp/hitch-v4-pycache python3 -m compileall hitch tests
python3 -m hitch.demo prepare
python3 -m hitch.demo simulation "이번 주 내가 놓친 관계 신호를 점검해줘"
```
These checks validate the relationship-space, ingest, wiki, simulation, and daily/weekly wiring before Atlas review.

### 7. Telegram Runtime
The Telegram bot token is read from local `.env` as `HITCH_TELEGRAM_TOKEN`.
Do not print, commit, or copy the token into tracked files.

Validate local token/API access without starting the long-running bot:
```bash
python3 -m hitch --check
```

Start the bot locally:
```bash
python3 -m hitch
```

The bot supports:
- `/start` for onboarding and relationship-space creation
- `/daily` for one daily question path
- `/weekly` for a weekly report generated from accumulated local wiki signals
- `/space` for the active relationship-space summary

## Operator Notes
- Mac mini remains the actual runtime hub
- MacBook is the remote control surface
- vanilla `codex` is the default implementation execution path
- private data must remain outside remote git push boundaries
- use small coherent commits for product-building work
