# Heal record

heal-and-verify close for parser null deref.

Cure: triage-captured reproduction now passes (`python repro.py` → exit 0).
No new wounds: surrounding suite pass at pre-breakage scope (pytest -q → green).
Mechanism: VERIFIED root-cause — null guard missing at parse_edge; heal adds check.

BROKE: null deref on empty token | CAUSE: missing guard in parse_edge | HEAL: add null check, root | CAUGHT-BY: pytest repro | WOULD-HAVE-CAUGHT-SOONER: unit test for empty token
