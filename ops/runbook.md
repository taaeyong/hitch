# Runbook

## Purpose
This runbook describes how Hitch v4 is operated as a relationship understanding system on the Mac mini, with the user acting as a remote operator from a MacBook.

## Operating Assumption
- Mac mini is the execution hub
- MacBook is the remote operator surface
- Telegram is the primary user-facing interaction surface
- vanilla `codex` is the default implementation execution path
- private relationship data remains local-only unless explicitly sanitized

## Core Operational Areas
1. Telegram-facing interaction flow
2. relationship space state and metadata
3. raw txt ingest pipeline
4. wiki growth and persistence
5. simulation and weekly reporting
6. demo-safe artifact generation

## Main Operator Goals
- keep the bot runnable
- keep private data local-only
- keep the wiki evolving visibly during demo
- make recovery simple when Telegram/runtime issues occur
- maintain product tone and drift control during implementation

## Core Files to Know
- `spec/README.md`
- `spec/demo-run.md`
- `spec/simulation-run.md`
- `ops/boundaries.md`
- `ops/demo-flow.md`
- `ops/execution.md`
- `ops/recovery.md`

## Operator Checklist
Before a serious run or demo:
1. confirm private data boundaries
2. confirm Telegram bot process status
3. confirm raw/data directories exist
4. confirm relationship space data path is healthy
5. confirm latest wiki output is readable
6. confirm demo-safe artifact layer does not expose private data

## Current Launch Commands
Prepare local grounded rehearsal state:
```bash
python3 -m hitch.demo prepare
```

Run one grounded simulation feedback loop:
```bash
python3 -m hitch.demo simulation "이번 주 내가 놓친 관계 신호를 점검해줘"
```

Run the practical local rehearsal path:
```bash
python3 -m hitch.demo rehearse
```

Validate token/API reachability:
```bash
python3 -m hitch --check
```

Run the Telegram-first demo bot:
```bash
python3 -m hitch
```

The process stores relationship-space metadata, wiki signals, simulation feedback state, simulation records, graph payloads, and weekly reports under ignored local `data/` paths. Raw private files remain local-only and are not copied into tracked artifacts.

## Drift / Review Rule
Atlas may use prior product context and background understanding to guide implementation choices, resolve ambiguity, and review Codex output.
The spec does not need to be totally closed before work begins, as long as product-intent drift remains actively controlled.

## Execution Loop
The preferred operating loop for Hitch v4 is:
1. Atlas defines or sharpens scope, prompt, and spec boundaries
2. vanilla `codex` performs implementation work, creates commits, and pushes them promptly when the slice is safe and complete
3. Atlas monitors the repo, reviews drift and private-boundary safety, and intervenes only when there is meaningful risk or blockage
4. if needed, Atlas issues another focused iteration

### Role Split
- vanilla `codex`: first-pass implementer
- Atlas: product-memory-aware reviewer, operator, and ambiguity resolver

## Proactive Monitoring Rule
Atlas should not wait passively for explicit user requests when a meaningful review boundary has been crossed.
After a Ralph/Codex iteration or meaningful commit set, Atlas should proactively check for:
1. private data boundary risk
2. product drift toward generic chatbot behavior
3. simulation overclaim or fake-authority behavior
4. broken relationship-space assumptions
5. repo structure drift away from the current spec
6. suspiciously large or incoherent commits
7. blockers that are likely to waste the next iteration if not surfaced early

## Escalation Rule
Atlas should proactively notify the user when there is:
- a real blocker
- a private-boundary risk
- a meaningful design drift
- a recovery issue
- a decision that materially affects the next iteration

Atlas should NOT create an unnecessary commit or push bottleneck.
If Codex can safely commit and push within repo/spec boundaries, Atlas should let it proceed and focus on monitoring, review, interruption, and recovery.

## Interruption Rule
If a task is consuming too much time, creating unnecessary risk, or blocking clearly more important downstream work, Atlas may interrupt that line of work and redirect the iteration toward the safer or higher-leverage path.
This especially applies to risky or overly time-consuming work around private conversation parsing, raw ingest accidents, or premature complexity in data handling.

## Atlas Control Responsibility
Atlas has an important operator role in keeping Codex workstreams productive rather than passively observing them.
Atlas should actively supervise implementation progress, preserve continuity, and intervene when needed so the workstream does not stall, drift, or get trapped in low-value subproblems.

### Practical Meaning
- Atlas should help keep the implementation loop moving
- Atlas may cut off a bad or overlong sub-task and redirect effort
- Atlas may step in with product judgment when uninterrupted autonomous work is no longer serving the real goal
- Atlas is responsible not only for review after the fact, but also for active control when needed to protect momentum and goal attainment

## Lesson Learned: Trust Gate Handling
When Codex opens a directory-trust confirmation for a repo that Atlas and the user intentionally created and are actively operating, Atlas should proactively approve that trust gate instead of waiting on the user.
This is part of the operator/control responsibility.

## Execution Standard
Use vanilla `codex` as the default implementation path for Hitch v4 on this machine.

Practical notes:
- prefer direct `codex` execution over `omx ralph` for this repo because observability and git completion are more reliable
- prefer high reasoning effort, equivalent in spirit to the earlier `--xhigh` preference
- prefer `--yolo` when uninterrupted fast implementation is explicitly intended, equivalent in spirit to the earlier `--madmax` preference
- `omx ralph` remains available only as a fallback path

### Rule
- if the repo is intentionally created, expected, and under current operator control, Atlas should pass the trust confirmation immediately
- do not surface this as a user-blocking question unless the repo origin or safety is genuinely unclear
