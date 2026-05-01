# Demo Run Spec

## Purpose
This document defines the exact contract for the first end-to-end execution entrypoint of Hitch v4.

The goal is not a loose collection of helper scripts.
The goal is one clear runnable entrypoint that can be used for final rehearsal and then later moved into the main `hitch` submission repo.

In this repo language:
- `demo` means the stage where the user can actually use Hitch through Telegram
- `simulation` means the grounded loop where girlfriend data, wiki accumulation, and ping-pong-like partner estimation keep building relationship understanding over time

## Why this exists
Hitch v4 already has product docs, ontology direction, ingest direction, wiki direction, simulation direction, and Telegram demo direction.
What is still missing is a single executable flow that ties those pieces together into a real rehearsal path.

This runner should make it possible to:
1. prepare local runtime prerequisites
2. use local girlfriend relationship data as grounded source material
3. seed or refresh a relationship space
4. build minimal wiki/signal state from that source material
5. produce simulation-backed output from that grounded state
6. export graph-ready demo artifacts
7. run or prepare the Telegram-first demo path

## Output Shape
The implementation must provide one obvious primary entrypoint.
Required shape:
- `python -m hitch.demo`

Subcommands must be:
- `python -m hitch.demo prepare`
- `python -m hitch.demo telegram`
- `python -m hitch.demo rehearse`

Default preference is a Python module entrypoint, not a bash-only implementation.
Bash wrappers are acceptable only as thin wrappers and must delegate into the Python runtime code.

## Runner Goal
The runner should support the full practical rehearsal path for Hitch v4:
1. verify local environment
2. verify local token availability
3. verify raw girlfriend csv availability
4. create or refresh relationship space state
5. run minimal ingest from the girlfriend csv
6. update local wiki/signal/pattern/report-ready state
7. generate at least one graph-ready artifact
8. make Telegram-first demo execution immediately possible

## Grounding Rules
The first e2e runner is grounded primarily on:
- `raw/girlfriend_kakaotalk.csv`

Secondary/local-only inputs may exist later, but the first runner should be built around the girlfriend csv because that is the current strongest grounded rehearsal source.

The runner must not assume public-safe data.
It must assume the source material is private and local-only.

## Required Local Inputs
The runner must expect these to exist locally:
- `.env`
- `raw/girlfriend_kakaotalk.csv`

Optional later inputs may include:
- `raw/mother_kakaotalk.csv`
- other txt/csv files

## Required Environment Handling
The runner must:
- read Telegram token from local `.env`
- never print the token value
- never write the token into tracked files
- fail clearly if the token is absent when Telegram runtime is requested

Preferred environment variable name:
- `HITCH_TELEGRAM_TOKEN`

## Required Runtime Modes
The runner should support at least these modes.

### 1. `prepare`
Purpose:
- verify local inputs
- prepare local directories
- create or refresh relationship space
- ingest the grounded girlfriend csv into minimal local structures
- build wiki/signal state
- export graph-ready artifact

Expected result:
- local data structures exist
- graph-ready artifact exists
- the repo is ready for demo execution

### 2. `telegram`
Purpose:
- start the Telegram-first Hitch runtime using prepared state

Expected result:
- the bot can be reached from Telegram
- `/start` and the main demo path can be exercised

### 3. `rehearse`
Purpose:
- run the practical e2e rehearsal path in one command
- this must include `prepare`
- this must generate local simulation/report/graph-ready outputs
- this must leave the system in a Telegram-demo-ready state
- if feasible, it should also start the Telegram runtime directly

This mode is the real core deliverable.
If there is only one default mode, it should behave closest to `rehearse`.

## Demo Contract
`demo` is the stage where the user can actually use Hitch in Telegram.

The runner should support a real Telegram-first demo story close to this sequence:
1. Hitch has grounded local relationship material
2. Hitch has an active relationship space
3. Hitch has extracted minimal wiki/signal state
4. Hitch can answer in a Telegram-first style
5. the user can interact with Hitch through Telegram commands and replies
6. Hitch can export graph-ready or demo-safe structured artifact output

The demo should feel operational and usable, not like a static script.

## Relationship Space Contract
The runner must either create or refresh a single main relationship space for rehearsal.

Minimum setup target:
- relationship type: romantic
- partner label: partner or equivalent stable label
- one-line current relationship state
- daily delivery time
- love-language mode

The runner may hardcode or default some of these for rehearsal if needed, but the defaults must remain legible in code.

## Ingest Contract
The first implementation does not need a perfect KakaoTalk parser.
But it must do more than merely register file existence.

Minimum acceptable ingest behavior:
- consume the girlfriend csv
- extract at least a minimal usable set of structured records
- write parsed message records
- write signal candidates
- write relationship summary seed state
- write graph payload seed state
- leave visible local outputs that Atlas or the user can inspect

It is acceptable for this first runner to use a shallow or heuristic parser if it is clearly bounded and inspectable.

## Wiki / Signal Contract
The runner must produce visible local Hitch state from grounded input.
Minimum expected outputs:
- relationship space state
- signal-like accumulated records
- at least one summary/report-ready structure
- graph-ready export structure

The point is not full ontology perfection.
The point is visible, grounded, inspectable accumulation.

## Graph Artifact Contract
The runner must export at least one graph-ready artifact locally.
Preferred output shape:
- JSON payload under local ignored data paths

It does not need a polished graph UI yet.
But it should produce something clearly suitable for later visualization.

## Telegram Contract
The runner should make Telegram rehearsal straightforward.

Minimum expectation:
- after `prepare`, the bot can be started in a known good state
- `/start` should work
- onboarding or relationship-space setup should work
- one daily question should be reachable
- one user answer should produce a simulation-backed response
- one weekly/report output should be reachable

Preferred if feasible:
- the `rehearse` mode gets the system into the state needed for a real Telegram walk-through with minimal operator steps
- the Telegram flow should expose a visible loop command such as `/loop` for repeated simulation-driven updates
- the Telegram flow should expose graph or state visibility such as `/graph`

The Telegram rehearsal should feel like ongoing relationship maintenance, not a one-off quiz bot.

## Private Boundary Rules
The runner must not:
- commit `.env`
- commit raw csv/txt relationship files
- write private grounded artifacts into tracked paths
- generate remote-safe docs that accidentally quote private raw material

All grounded outputs from the real girlfriend csv should remain local-only unless explicitly sanitized.

## Implementation Bias
The implementation should prefer:
- simple Python
- obvious file layout
- explicit local paths
- inspectable intermediate outputs
- a single understandable operator path

over:
- framework complexity
- hidden orchestration magic
- premature parser sophistication
- overengineered abstractions

## Codex Execution Contract
When Codex implements this runner, execute it in the aggressive implementation mode equivalent to yolo + xhigh.

Practical command intent:
- use `codex --yolo`
- use the highest available reasoning effort for this run, equivalent in spirit to xhigh

## Commit / Push Rule for Codex
When Codex implements this runner:
- use `--yolo`
- use the highest available reasoning effort for this run
- commit in very small coherent slices
- push frequently
- do not wait until the whole runner is perfect before committing

Suggested commit slices:
1. runner skeleton / CLI contract
2. local env and input checks
3. relationship space prepare flow
4. csv ingest flow
5. wiki/signal accumulation flow
6. simulation flow
7. graph export flow
8. Telegram rehearsal wiring
9. README / execution docs sync

## Love-Language Update Loop Contract
The runner should not treat love-language understanding as frozen after setup.
It should support ongoing update from repeated interaction.

Minimum expected behavior:
- repeated answers can influence local signal state
- the system can accumulate evidence about how love is expressed and received
- later simulations can benefit from earlier interaction deltas
- the wiki can become richer as the loop continues

If exact love-language scoring is too heavy for this pass, use a lighter interpretation-delta model rather than omitting the update loop entirely.

## Success Criteria
This spec is satisfied when all of the following are true:
1. there is one obvious e2e entrypoint
2. the entrypoint can prepare grounded local state from `raw/girlfriend_kakaotalk.csv`
3. the entrypoint can produce wiki/signal/simulation/graph-ready outputs locally
4. the simulation can feed meaningful deltas back into local state rather than ending as a disposable one-off answer
5. the Telegram-first demo can be run from the prepared state
6. the entire flow is legible enough to rehearse before migration into the main `hitch` repo

## Non-Goals for this pass
Do not require in this pass:
- perfect KakaoTalk parsing
- production-grade graph UI
- fully generalized multi-relationship ingest framework
- public-safe packaging of private grounded outputs
- full bidirectional partner participation

This pass is about building the practical grounded rehearsal runner.
