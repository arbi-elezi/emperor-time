# reproduce-and-bisect fixtures

Prove reproduce-and-bisect HARD-GATE (`reproduce.py --reject-no-repro` /
`--reject-no-combat-ledger` / `--check-reproduce`).

| Fixture | Expect |
|---|---|
| `repro-ok.md` | PASS — fingerprint + combat ledger |
| `repro-no-fingerprint.md` | FAIL — reproduce signal, missing fingerprint |
| `repro-no-combat.md` | FAIL — fingerprint present, missing combat ledger |
| `repro-vacuous.md` | PASS vacuous — no reproduce signal |
| `task-ok/` | PASS — ledger fingerprint + combat ledger |
| `task-no-fingerprint/` | FAIL — reproduce claimed, no fingerprint |
| `task-no-combat/` | FAIL — fingerprint ok, no combat ledger |
