# Task Ledger — triage-ok

## G0
- Origin: eval fixture
- Task: prove holy triage hard-gate accept path
- Holy: triage

## G1 Acceptance criteria
1. triage.py exits 0 on this task dir

## Out of scope
- live production incident

## G2
Size: trivial

## G3
Build: fixtures only

## G4
- Self-critique: n/a fixture
- Verdict: PASS

## Triage
TRIAGE 2026-09-29T01:10+02
Broke: TypeError NoneType in parse_edge         Noticed by: `python repro.py`
Last-good: v0.4.138 @ d07ac02                   First-bad: WIP
Snapshot: rescue/task-triage-ok HEAD             Class: local
Agents halted: none
