# process-healing fixtures

Prove holy process-healing HARD-GATE (`process_heal.py --reject-no-register` /
`--reject-no-reentry` / `--check-process-heal`).

| Fixture | Expect |
|---|---|
| `process-ok.md` | PASS — register entry + RE-ENTERED seam |
| `process-no-register.md` | FAIL — process signal, missing register |
| `process-no-reentry.md` | FAIL — register present, missing RE-ENTERED |
| `process-vacuous.md` | PASS vacuous — no process-healing signal |
| `task-ok/` | PASS — ledger register + RE-ENTERED |
| `task-no-register/` | FAIL — process claimed, no register |
| `task-no-reentry/` | FAIL — register ok, no RE-ENTERED |
