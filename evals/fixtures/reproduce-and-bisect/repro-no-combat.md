# Fingerprint without combat ledger

reproduce-and-bisect close.

REPRO: `python repro.py` fails on demand with fingerprint `AssertionError: expected 2 got 0`.

Cause isolated: off-by-one. (No H#: predict/ran/saw combat ledger line.)
