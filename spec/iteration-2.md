# Iteration 2 Implementation Brief

## Goal
Turn the iteration-1 scaffold into a minimally real, inspectable relationship-system core.

This iteration focuses on:
- upgrading skeleton modules into usable domain logic
- making relationship space, ingest, wiki, and simulation shapes concretely connected
- preserving private-boundary safety while increasing product realism
- preparing a stronger handoff point for the noon Ralph run

This is still not a full product-completion iteration.
It is a structure-to-usable-core iteration.

## What Iteration 1 Already Landed
Iteration 1 already created:
- repo scaffold for `raw/`, `data/`, `ontology/`, `hitch/`, `prompts/`, `tests/`
- baseline relationship space / ingest / wiki / simulation / flow module layout
- baseline tests
- ontology vocabulary file
- private-boundary-aware `.gitignore`

Iteration 2 must build on that instead of re-scaffolding from scratch.

## Must Deliver

### 1. Relationship Space: Make It Real
Upgrade relationship space from basic skeleton to a usable domain object.

Must include:
- explicit relationship-space model
- minimum creation set validation
- load/save helpers
- deterministic storage path convention
- clear separation between relationship metadata and derived summaries

Minimum creation set remains:
1. relationship type
2. partner label/name
3. one-line current relationship state
4. daily delivery time
5. simple vs deep love-language mode

### 2. Ingest: Make txt/csv Registration Actually Useful
Upgrade ingest from placeholder shape to minimal working ingestion utilities.

Must include:
- register txt/csv source files with metadata
- recognize source type and relationship target
- normalize source metadata into a stored record
- create a clean seam for future parser/segmenter logic

Do NOT build a generalized production KakaoTalk parser.
Do NOT overfit to one raw file format in a way that will break the future ingest direction.

### 3. Wiki / Intermediate Data: Connect the Layers
Make the wiki/storage layer minimally real.

Must include usable storage shapes or persistence helpers for:
- people
- relationships
- episodes
- patterns
- signals
- summaries
- reports

Also make the intermediate structured data layer visibly connected to:
- ingest outputs
- relationship space
- simulation inputs

The key is not depth, but clear connection and inspectable structure.

### 4. Simulation: Grounded Interface, Not Theater
Upgrade simulation from pure placeholder to grounded interface logic.

Must include:
- simulation input model
- simulation output model
- run record
- snapshot record
- effect record
- a function or service boundary that assembles simulation input from stored context

Do NOT create fake-confident partner-answer behavior.
Simulation should remain framed as partner perspective estimation.

### 5. Daily / Weekly Flow: Tie Them to Relationship Space
Upgrade flow placeholders so they are relationship-space aware.

Must include:
- daily question flow entrypoint using relationship space
- weekly check flow entrypoint using relationship space
- weekly report placeholder with explicit output shape
- partner-answer reveal placeholder with explicit safe/demo framing

These can still be lightweight, but they must no longer feel like generic chatbot entrypoints.

### 6. Tests: Raise Them Above Pure Placeholder Level
Strengthen tests so the repo proves actual usable structure.

Must cover at least:
- relationship space creation/validation
- ingest registration behavior
- wiki/storage path or persistence expectations
- simulation model assembly shape
- daily/weekly flow basic wiring

### 7. Ops / Reviewability Alignment
Update docs only where needed to reflect the now-more-real implementation.

Focus on:
- keeping ops docs aligned with actual repo behavior
- preserving Atlas review-before-push workflow
- leaving visible TODOs where depth is intentionally deferred

## Do Not Do In This Iteration
- full Telegram UX implementation
- full product copywriting pass
- full graph visualization
- advanced retrieval system
- advanced pattern induction
- advanced signal extraction engine
- fake partner theater
- broad storage abstraction overkill

## Important Constraints

### Private Data Boundary
- do not commit real relationship raw data
- do not create code paths that accidentally move raw private data into demo-safe tracked artifacts
- keep repo safe for remote push

### Product Boundary
- relationship space must remain a first-class product concept
- wiki must not degrade into a raw dump archive
- simulation must stay grounded, soft, and uncertainty-aware
- Hitch should remain a relationship understanding system, not a generic assistant shell

### Review Boundary
- prefer explicit, readable, inspectable logic over clever abstraction
- prefer domain naming that matches current Hitch v4 product intent
- leave obvious seams for iteration 3 instead of pretending to finish everything now

## Completion Criteria
Iteration 2 is successful if:
1. relationship space is a usable, validated domain object
2. ingest registration for txt/csv actually works in a minimal way
3. wiki/intermediate storage layers are connected and inspectable
4. simulation has grounded input/output/run structures and assembly seams
5. daily/weekly flows are relationship-space aware
6. tests demonstrate real structure instead of pure placeholder existence
7. repo remains safe to push and easy for Atlas to review

## Commit Style
- use small coherent commits
- explicit commit messages only
- no private data in commits
- do not push automatically

## Why This Iteration Exists
Iteration 1 proved the scaffold.
Iteration 2 should prove that the scaffold can actually behave like the beginning of a real relationship operating system without collapsing into either generic bot code or fake overbuilt complexity.
