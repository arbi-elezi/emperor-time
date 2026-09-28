# heal-and-verify fixtures

Prove heal-and-verify HARD-GATE (`heal_verify.py --reject-no-triad` /
`--reject-no-postmortem` / `--check-heal`).

| Fixture | Expect |
|---|---|
| `heal-ok.md` | PASS — triad + postmortem |
| `heal-no-triad.md` | FAIL — heal signal, missing triad |
| `heal-no-postmortem.md` | FAIL — triad present, missing postmortem |
| `heal-vacuous.md` | PASS vacuous — no heal signal |
| `task-ok/` | PASS — ledger triad + postmortem |
| `task-no-triad/` | FAIL — heal claimed, no triad |
| `task-no-postmortem/` | FAIL — triad ok, no postmortem |
