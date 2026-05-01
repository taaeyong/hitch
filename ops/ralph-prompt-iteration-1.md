# Ralph Prompt - Iteration 1

This prompt is intended to be used through the default implementation execution path:
- `omx ralph`

You are implementing iteration 1 of Hitch v4 in `/Users/taaeyong/projects/hitch-test-v4`.

Read first:
- `spec/README.md`
- `spec/iteration-1.md`
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
Your job is to complete iteration 1 only: establish a strong implementation scaffold for Hitch v4.

## Iteration 1 priorities
1. create missing repo scaffold for raw/data/ontology/hitch/prompts/tests
2. implement relationship space domain skeleton
3. implement raw ingest skeleton for txt + csv source material
4. implement wiki / intermediate structured data skeleton
5. implement simulation interface + persistence skeleton
6. create daily / weekly domain flow entry skeletons
7. ensure ops docs and implementation structure align
8. add basic tests or test placeholders for the new structure

## Important product rules
- Hitch is a relationship understanding system, not a generic chatbot
- relationship space is the core operating unit
- simulation is centered on partner perspective estimation, not theatrical imitation
- visible wiki growth is part of the product and demo value
- open conversation should remain relationship-aware when useful, but should not force fake references
- preserve Hitch tone and product identity in naming and structure decisions

## Important boundaries
- do NOT commit any real private relationship data
- girlfriend / mother raw data and private wiki material must remain outside remote-safe artifacts
- treat current source material as potentially private
- mock answers must not be presented as real partner answers

## Commit / push rule
- make small coherent commits during implementation
- use explicit commit messages
- do NOT push automatically
- Atlas will review before any push
- leave clear TODOs where logic is intentionally deferred

## Risk / blocker handling rule
- if you encounter a likely blocker, do not silently bulldoze through it
- if a private-boundary risk appears, stop short of unsafe completion and document it clearly
- if a design choice may create spec drift, leave a visible note or TODO for Atlas review
- if ambiguity appears, prefer the implementation that preserves structure and reviewability over premature completeness

## What NOT to do in this iteration
- do not build a full production KakaoTalk parser
- do not build a polished Telegram UX
- do not build a full graph visualization UI
- do not overengineer storage abstractions
- do not implement fake-high-confidence partner simulation
- do not drift into a generic assistant architecture

## Expected outcome
At the end of iteration 1, the repo should have:
- a clean scaffold matching the current spec structure
- a real relationship space domain shape
- a recognizable ingest starting point for txt/csv input
- a wiki/intermediate data persistence shape
- a simulation persistence shape
- daily/weekly placeholders
- tests or test placeholders
- implementation-ready structure for deeper later iterations

If something is ambiguous, prefer the option that best preserves product intent and leaves the repo easier for Atlas to review and extend.
