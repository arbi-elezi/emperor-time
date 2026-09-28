# thoughttrail-super-context fixtures

HARD-GATE fixtures for `scripts/lib/context.py`.

| Path | Expect |
|---|---|
| `repo-ok/` | `--check-context` and `--check-trail` PASS (built graph + trail) |
| `repo-no-graph/` | `--check-context` FAIL (CONTEXT READY claimed, no sqlite/l0) |
| `repo-no-trail/` | `--check-trail` FAIL (thoughttrail claimed, empty/missing trail) |
| `task-ok/` | ledger claims activity; nested `.emperor` ready → PASS |
| `task-no-graph/` | ledger CONTEXT READY; missing graph → FAIL check-context |
| `task-vacuous/` | no activity markers → vacuous PASS |
