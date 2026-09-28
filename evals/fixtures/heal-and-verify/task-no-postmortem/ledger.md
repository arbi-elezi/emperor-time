# Task Ledger — heal-no-postmortem

## G0
- Origin: eval fixture
- Task: prove heal-and-verify rejects missing postmortem
- Holy: heal-and-verify

## G1 Acceptance criteria
1. heal_verify.py exits 1

## Heal
Cure: reproduction now passes.
No new wounds: full suite pass.
Mechanism: VERIFIED root-cause — race in waiter.
