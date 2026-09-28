# Task Ledger — heal-ok

## G0
- Origin: eval fixture
- Task: prove heal-and-verify hard-gate accept path
- Holy: heal-and-verify

## G1 Acceptance criteria
1. heal_verify.py exits 0 on this task dir

## Out of scope
- live production incident

## G2
Size: trivial

## G3
Build: fixtures only

## G4
- Self-critique: n/a fixture
- Verdict: PASS

## Heal
Cure: triage-captured reproduction now passes (`python repro.py` → exit 0).
No new wounds: surrounding suite pass at pre-breakage scope.
Mechanism: VERIFIED root-cause — missing null guard; heal adds check.

BROKE: null deref | CAUSE: missing guard | HEAL: null check, root | CAUGHT-BY: pytest | WOULD-HAVE-CAUGHT-SOONER: empty-token unit test
