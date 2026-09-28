# Task Ledger — no combat

## G0
- Origin: eval fixture
- Task: prove reproduce-and-bisect rejects missing combat ledger
- Holy: reproduce-and-bisect

## Reproduce
REPRO: `python repro.py` fails on demand with fingerprint `AssertionError: boom`.

Cause isolated: off-by-one. No combat ledger H# line.
