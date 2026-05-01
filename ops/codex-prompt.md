# Codex Prompt

This prompt is intended to be used through the default implementation execution path:
- vanilla `codex`
- prefer `--yolo` when uninterrupted fast implementation is desired
- prefer high reasoning effort, equivalent in spirit to earlier xhigh usage

You are implementing Hitch v4 in `/Users/taaeyong/projects/hitch-test-v4`.

Read first:
- `README.md`
- `spec/README.md`
- `spec/product.md`
- `spec/relationship-space.md`
- `spec/wiki.md`
- `spec/simulation.md`
- `spec/ontology.md`
- `spec/ingest.md`
- `spec/demo.md`
- `spec/ops.md`
- `ops/runbook.md`
- `ops/boundaries.md`
- `ops/demo-flow.md`
- `ops/execution.md`

Your job is to build the intended Hitch v4 demo, not just a partial scaffold.
The target is a Telegram-first runnable demo that expresses the actual product direction.

## Primary implementation target
Build a working repo that includes:
1. runnable Telegram bot entrypoint
2. relationship space creation and persistence
3. daily question flow
4. weekly report flow
5. simulation-backed partner-perspective output
6. visible wiki / intermediate structured data growth
7. graph-ready structured outputs or demo-safe visualization artifacts if feasible
8. clear local run instructions

## Important product rules
- Hitch is a relationship understanding system, not a generic chatbot
- relationship space is the core operating unit
- simulation is centered on partner perspective estimation, not theatrical imitation
- wiki growth should remain visible and structured
- preserve Hitch tone and product identity in naming and interaction copy
- prefer grounded, inspectable logic over broad abstraction
- runnable value matters more than architectural cleverness

## Important boundaries
- do NOT commit any real private relationship data
- girlfriend / mother raw data and private wiki material must remain outside remote-safe artifacts
- treat current source material as potentially private
- do not let wiki storage collapse into a raw dump archive
- mock answers must not be presented as real partner answers
- never print or commit real bot secrets from local `.env`

## Commit / push rule
- make small coherent commits during implementation
- use explicit commit messages
- commit and push from inside Codex when the current slice is safe, coherent, and within repo/spec boundaries
- leave clear TODOs where logic is intentionally deferred
- do not wait until the end to make one large commit
- create a commit whenever one meaningful domain slice is completed
- preferred slices are:
  1. runtime/config/bootstrap
  2. relationship space
  3. wiki/storage layer
  4. simulation
  5. Telegram flow wiring
  6. tests/docs/run instructions
  7. graph-ready artifact layer if included
- prefer even smaller slices when natural, as long as each commit still leaves the repo in a sane reviewable state
- avoid going more than roughly 15 to 20 minutes without producing a coherent commit if meaningful progress has been made
- if you finish a meaningful slice, commit and push it before moving deeply into the next slice

## Risk / blocker handling rule
- if you encounter a likely blocker, do not silently bulldoze through it
- if a private-boundary risk appears, stop short of unsafe completion and document it clearly
- if a design choice may create spec drift, leave a visible note or TODO for Atlas review
- if ambiguity appears, prefer the implementation that preserves structure, reviewability, and product intent over premature completeness

## What NOT to do
- do not build a full production KakaoTalk parser
- do not over-polish Telegram UX before the real flow works
- do not overengineer storage abstractions
- do not implement fake-high-confidence partner simulation
- do not drift into a generic assistant architecture

## Expected outcome
At the end of the run, the repo should have:
- a runnable Telegram-first Hitch demo
- local token check and run commands
- inspectable relationship-space, wiki, and simulation outputs
- tests proving core flow wiring
- commit/push history in small coherent slices
- repo docs updated to reflect the actual run path

If something is ambiguous, prefer the option that best preserves product intent and leaves the repo easier for Atlas to review and extend.
