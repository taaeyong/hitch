# Simulation Spec

## Primary Purpose
The primary purpose of simulation is partner-perspective estimation, not theatrical answer mimicry.

Simulation should support:
1. partner answer reconstruction when useful
2. partner perspective estimation as the main function
3. relationship gap interpretation support
4. demo and visualization support

## Core Framing
Simulation is a time-compressed virtual run of the relationship-understanding service.
It approximates longer-term relationship understanding using available material rather than waiting months for accumulation.

## Source of Truth
In current one-way v4:
- primary source for simulated partner answers is raw text material
- wiki context may assist but should not replace raw textual grounding

## Input Set
1. current question or scenario
2. relevant raw text snippets
3. related episodes
4. stable patterns
5. current relationship summary

## Output Set
1. partner likely answer
2. partner likely feeling or state
3. why this likely matters to them
4. confidence or uncertainty level

## Style
- mixed style
- slight reflection of partner tone is okay
- default center is meaning and intent, not impersonation

## Confidence Exposure
- confidence should be expressed implicitly, not as an explicit score
- use soft interpretive language when uncertain

## Safety Rules
1. do not make strong claims without raw evidence support
2. do not present the partner's emotional state as a certainty
3. avoid overreaching relationship diagnosis from thin signal
4. do not package mock answers as if they were real partner answers
5. when signal is weak, fall back toward more general coaching

## Persistence Structure
1. simulation_runs
2. simulation_snapshots
3. simulation_effects

### Meaning
- `simulation_runs`: concrete execution record with input, output, basis, and confidence
- `simulation_snapshots`: summarized simulation state of a relationship space at a moment
- `simulation_effects`: what changed in wiki, patterns, summaries, or reports because of the simulation

## Wiki Update Policy
- simulation outputs may update the wiki layer directly in v4
- this is acceptable because the environment is exploratory and time-compressed
- visible wiki growth is part of demo value
