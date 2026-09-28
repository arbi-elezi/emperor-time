# Task Ledger — repro-ok

## G0
- Origin: eval fixture
- Task: prove reproduce-and-bisect hard-gate accept path
- Holy: reproduce-and-bisect

## G1 Acceptance criteria
1. reproduce.py exits 0 on this task dir

## Out of scope
- live production incident

## G2
Size: trivial

## G3
Build: fixtures only

## G4
- Self-critique: n/a fixture
- Verdict: PASS

## Reproduce
REPRO: `python repro.py` fails on demand with fingerprint `TypeError: NoneType`.

H1: null guard missing in parse_edge | predict: add guard → green | ran: python repro.py | saw: TypeError | H1 VERIFIED

Cause isolated + mechanism articulated.
