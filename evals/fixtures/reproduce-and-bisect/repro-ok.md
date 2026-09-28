# Reproduce record

reproduce-and-bisect close for parser null deref.

REPRO: `python repro.py` fails on demand with fingerprint
`TypeError: 'NoneType' object is not subscriptable`.

Combat ledger:
H1: cause in parse_edge null guard | predict: add guard → repro passes | ran: python repro.py | saw: TypeError NoneType | H1 OPEN
H2: null at token stream boundary | predict: empty token triggers | ran: python repro.py --empty | saw: same TypeError | H2 VERIFIED

Cause isolated: missing null guard in parse_edge. Mechanism: empty token yields None into subscript.
