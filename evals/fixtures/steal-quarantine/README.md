# steal-quarantine fixtures

Prove Steal quarantine admission HARD-GATE (`quarantine.py --reject-unquarantined` /
`--check-quarantine`).

| Fixture | Expect |
|---|---|
| `admission-ok.md` | PASS — CONJECTURE + ADMITTED/REJECTED |
| `admission-missing.md` | FAIL — steal signal, no admission |
| `task-ok/` | PASS — runs + CONJECTURE + admission |
| `task-no-conjecture/` | FAIL — missing CONJECTURE start |
| `task-unquarantined/` | FAIL — missing quarantine layout |
| `vacuous.md` / `task-vacuous/` | SKIP vacuous — no steal activity (honest N/A) |
