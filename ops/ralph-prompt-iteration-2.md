# Ralph Prompt - Iteration 2

This prompt is intended to be used through the default implementation execution path:
- `omx ralph`

You are implementing iteration 2 of Hitch v4 in `/Users/taaeyong/projects/hitch-test-v4`.

Read first:
- `spec/README.md`
- `spec/iteration-2.md`
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

Your job is NOT to complete the whole product.
Your job is to complete iteration 2 only: turn the scaffold into a minimally real, inspectable relationship-system core.

## Iteration 2 priorities
1. upgrade relationship space into a usable validated domain object
2. make txt/csv ingest registration minimally real
3. connect wiki and intermediate structured data layers
4. upgrade simulation into a grounded interface and persistence seam
5. make daily / weekly flows relationship-space aware
6. strengthen tests so they prove actual wiring, not only placeholders
7. keep the repo readable, reviewable, and safe for Atlas review

## Important product rules
- Hitch is a relationship understanding system, not a generic chatbot
- relationship space is the core operating unit
- simulation is centered on partner perspective estimation, not theatrical imitation
- wiki growth should remain visible and structured
- preserve Hitch tone and product identity in naming and structure decisions
- prefer grounded, inspectable logic over broad abstraction

## Important boundaries
- do NOT commit any real private relationship data
- girlfriend / mother raw data and private wiki material must remain outside remote-safe artifacts
- treat current source material as potentially private
- do not let wiki storage collapse into a raw dump archive
- mock answers must not be presented as real partner answers

## Commit / push rule
- make small coherent commits during implementation
- use explicit commit messages
- commit and push from inside Ralph/Codex when the current slice is safe, coherent, and within repo/spec boundaries
- leave clear TODOs where logic is intentionally deferred
- do not wait until the end to make one large commit
- create a commit whenever one meaningful domain slice is completed
- preferred commit slices in this iteration are:
  1. relationship space
  2. ingest registration
  3. wiki/storage wiring
  4. simulation interface
  5. daily/weekly flow wiring
  6. tests/docs alignment
- prefer even smaller slices when natural, as long as each commit still leaves the repo in a sane reviewable state
- avoid going more than roughly 15 to 20 minutes without producing a coherent commit if meaningful progress has been made
- if you finish a meaningful slice, commit and push it before moving deeply into the next slice
- Atlas will monitor for drift and boundary issues, but should not be treated as the default push gate for low-risk progress

## Risk / blocker handling rule
- if you encounter a likely blocker, do not silently bulldoze through it
- if a private-boundary risk appears, stop short of unsafe completion and document it clearly
- if a design choice may create spec drift, leave a visible note or TODO for Atlas review
- if ambiguity appears, prefer the implementation that preserves structure, reviewability, and product intent over premature completeness

## What NOT to do in this iteration
- do not build a full production KakaoTalk parser
- do not build polished Telegram UX
- do not build a full graph visualization UI
- do not overengineer storage abstractions
- do not implement fake-high-confidence partner simulation
- do not drift into a generic assistant architecture

## Expected outcome
At the end of iteration 2, the repo should have:
- a usable relationship space domain core
- minimal working txt/csv ingest registration
- connected wiki/intermediate storage layers
- grounded simulation input/output/run structures
- relationship-space-aware daily/weekly flows
- stronger tests demonstrating actual wiring
- a repo state that Atlas can meaningfully review for the noon Ralph run

If something is ambiguous, prefer the option that best preserves product intent and leaves the repo easier for Atlas to review and extend.
