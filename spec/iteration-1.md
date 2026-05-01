# Iteration 1 Implementation Brief

## Goal
Set up `hitch-test-v4` as a minimal but implementation-ready relationship operating system scaffold.

This iteration focuses on:
- landing the current spec into repo structure
- creating scaffolding for raw txt ingest, relationship space, wiki, simulation, and ops
- establishing a clean foundation for later Ralph/Codex-driven execution

This is a foundation iteration, not a full product-completion iteration.

## Must Deliver

### 1. Repo Scaffold
Ensure the repo has clear top-level structure for:
- `spec/`
- `raw/`
- `data/`
- `ontology/`
- `hitch/`
- `prompts/`
- `ops/`
- `tests/`

### 2. Raw/Data Layout
Create baseline directories for:
- `raw/kakao/girlfriend/`
- `raw/kakao/mother/`
- `data/parsed/`
- `data/episodes/`
- `data/signals/`
- `data/patterns/`
- `data/summaries/`
- `data/reports/`
- `data/graph/`
- `data/simulations/`

Current repository reality may include source material as csv files as well as txt files.
Iteration 1 should therefore treat raw relationship input as `txt + csv` compatible, while still keeping the longer-term ingest framing centered on rough human-dropped conversation material.

### 3. Relationship Space Skeleton
Implement the basic domain shape for a relationship space, including:
- relationship metadata model
- load/save path
- minimum creation set structure

Minimum creation set:
1. relationship type
2. partner label
3. one-line current relationship state
4. daily delivery time
5. simple vs deep love-language mode

### 4. Raw Ingest Skeleton
Create a minimal ingest entry layer that can:
- register raw txt or csv files
- load raw txt or csv files
- store source metadata
- expose future parser/segmenter hooks

A complete general KakaoTalk parser is not required in this iteration.
The main goal is to recognize and normalize the currently available source-material shape without overcommitting to a fully generalized ingestion engine yet.

### 5. Wiki / Memory Skeleton
Create storage structure for:
- people
- relationships
- episodes
- patterns
- signals

Also create the basis for the intermediate structured data layer used for simulation, retrieval, and graph materialization.

### 6. Simulation Interface Skeleton
Create the basic structures for:
- simulation input model
- simulation output model
- simulation run record
- simulation snapshot
- simulation effects

No need to implement a high-quality partner simulation engine yet.

### 7. Daily / Weekly Flow Skeleton
Create basic domain flow entrypoints for:
- daily question flow
- weekly check flow
- weekly report placeholder
- partner answer reveal placeholder

These may be skeletal as long as the structure is explicit.

### 8. Ops Docs
Create or complete:
- `ops/runbook.md`
- `ops/execution.md`
- `ops/recovery.md`
- `ops/boundaries.md`
- `ops/demo-flow.md`

### 9. Test Skeleton
Create baseline tests or test placeholders for:
- relationship space
- ingest
- wiki persistence
- simulation models
- weekly reporting

## Do Not Do In This Iteration
- full production-grade Kakao parser
- advanced signal extraction
- advanced pattern induction
- polished graph UI
- full Telegram onboarding polish
- overengineered storage abstraction
- fake partner-answer behavior presented as real

## Important Constraints

### Private Data Boundary
- girlfriend and mother raw txt / private wiki data must not be pushed to remote git
- repository structure must support private-local-only data boundaries

### Product/Tone Boundary
- Hitch is a relationship understanding system, not a generic chatbot
- simulation centers on partner perspective estimation, not theatrical imitation

### Safety Boundary
- do not present mock answers as real partner answers
- do not make strong claims on weak signal

## Completion Criteria
Iteration 1 is successful if:
1. repo structure is in place
2. spec and implementation layout are connected
3. relationship space exists as a real domain concept
4. raw ingest has a recognizable starting point
5. wiki storage shape exists
6. simulation persistence shape exists
7. ops docs exist
8. test scaffolding exists

## Commit Style
- use small coherent commits
- commit messages should be explicit
- do not include private relationship data

## Why This Iteration Exists
The purpose of iteration 1 is to finish the repo-level and architecture-level preparation needed before Ralph/Codex can safely build deeper product behavior.
It is effectively the last serious scaffold pass before stronger implementation acceleration.
