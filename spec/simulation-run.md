# Simulation Run Spec

## Purpose
This document defines the grounded relationship-learning run for Hitch v4.

`simulation` means the loop where girlfriend data, local wiki state, user prompts, and partner-perspective estimation keep updating relationship understanding over time.

## Primary Goal
The simulation run should do more than produce a single answer.
It should:
1. use local grounded relationship material
2. run a partner-perspective estimate
3. reflect the result back into local wiki/signal state
4. make later runs stronger through accumulated relationship understanding

## Grounding
Primary grounded source:
- `raw/girlfriend_kakaotalk.csv`

The simulation run must assume this data is private and local-only.

## Expected Interaction Shape
The preferred simulation shape is a light relationship ping-pong loop:
1. user-side answer or prompt
2. likely partner-side answer or reaction estimate
3. interpretation of gap or alignment
4. local wiki/signal/state update
5. optional next loop turn

## Required Commands / Modes
The final runtime should expose a simulation-oriented mode or command path, ideally through the shared primary entrypoint.

Preferred shapes:
- `python -m hitch.demo simulation`
- `/loop` inside Telegram for repeated simulation-driven updates
- `/graph` for graph/state visibility

## Minimum Simulation Contract
The simulation run must:
- use relationship-space state
- use ingested local grounded state
- produce simulation-backed output with uncertainty framing
- avoid fake certainty
- support repeated loop execution
- push meaningful deltas back into wiki-oriented local state

## Wiki Feedback Loop Contract
Simulation should not end as disposable output only.
It should write back at least:
- signal deltas
- interpretation deltas
- summary deltas
- open questions or follow-up prompts

Later runs should be able to benefit from those accumulated effects.

## Graph / Artifact Contract
The simulation run should export graph-ready or demo-safe structured artifacts that make the current relationship state visible.

Minimum acceptable outputs:
- graph payload seed or graph-ready JSON
- visible local artifact path
- enough structure for later visualization

## Love-Language Update Contract
Love-language understanding must not be frozen after setup.
Repeated interaction should be able to update local interpretation state over time.

If exact scoring is too heavy for this pass, a lighter delta-based interpretation model is acceptable.

## Success Criteria
This spec is satisfied when all of the following are true:
1. simulation can be run from grounded girlfriend data
2. simulation can produce a partner-perspective estimate
3. simulation can push meaningful results back into wiki/state
4. repeated runs can strengthen later interaction quality
5. graph-ready artifact output is produced locally
