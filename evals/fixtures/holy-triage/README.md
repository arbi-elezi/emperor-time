# holy-triage fixtures

Prove holy triage HARD-GATE (`triage.py --reject-no-triage` /
`--reject-no-snapshot` / `--check-triage`).

| Fixture | Expect |
|---|---|
| `triage-ok.md` | PASS — full triage block + snapshot |
| `triage-no-block.md` | FAIL — triage signal, missing block fields |
| `triage-no-snapshot.md` | FAIL — block fields present, missing Snapshot |
| `triage-vacuous.md` | PASS vacuous — no triage signal |
| `task-ok/` | PASS — ledger triage block + snapshot |
| `task-no-triage/` | FAIL — triage claimed, incomplete block |
| `task-no-snapshot/` | FAIL — block ok, no Snapshot |
