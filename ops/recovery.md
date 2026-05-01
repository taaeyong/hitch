# Recovery

## Purpose
This document defines the basic recovery posture for Hitch v4 when runtime, data, or demo issues appear.

## Recovery Principles
1. protect private relationship data first
2. restore a minimally working Telegram/runtime path quickly
3. preserve readable wiki state whenever possible
4. prefer simple recovery steps over heroic complexity in early iterations

## Common Failure Areas
### 1. Telegram Runtime Failure
Possible symptoms:
- bot does not respond
- stale updates replay unexpectedly
- polling conflict appears

Recovery posture:
- check whether another polling process is already running
- stop duplicate runtime processes
- restart the intended runtime cleanly
- verify that pending updates or stale queues are not causing misleading behavior

### 2. Raw Ingest Failure
Possible symptoms:
- txt files are present but not recognized
- parser output is empty or malformed
- source metadata is missing

Recovery posture:
- verify raw file placement under expected directories
- verify that the ingest entrypoint recognizes the file
- inspect parse-ready outputs before attempting deeper extraction

### 3. Wiki / Data Corruption Risk
Possible symptoms:
- malformed structured outputs
- invalid summary shapes
- broken graph payloads

Recovery posture:
- do not push questionable data artifacts remotely
- isolate the problematic generated outputs
- preserve raw inputs and prior known-good summaries
- rebuild derived layers from raw or earlier structured states if needed

### 4. Simulation Drift or Nonsense Output
Possible symptoms:
- overconfident partner claims
- weakly grounded simulation
- fake-real answer confusion

Recovery posture:
- fall back toward general coaching behavior
- reduce simulation authority
- inspect grounding inputs: raw snippets, episodes, patterns, summary
- do not treat questionable simulation as durable truth without review

### 5. Demo Safety Failure
Possible symptoms:
- private data appears in a pushable artifact
- demo-safe outputs are not actually sanitized

Recovery posture:
- stop any push immediately
- remove or isolate the unsafe artifact
- verify boundaries in `ops/boundaries.md`
- regenerate a sanitized replacement if needed

## Minimum Recovery Success Condition
Recovery is successful when:
- Telegram-facing path is usable again, or clearly isolated
- private data boundary is preserved
- relationship wiki state is not silently corrupted
- the next operator step is obvious
