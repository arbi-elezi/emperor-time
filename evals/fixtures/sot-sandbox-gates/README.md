# sot-sandbox-gates fixtures

HARD-GATE fixtures for SOT fetch-only + sandbox plan checkers.

| Path | Expect |
|---|---|
| `task-vacuous/` | `--check-sot` and `--check-sandbox` → SKIP (vacuous) |
| `task-sot-ok/` | `--check-sot` PASS (bare mirror + plugin.json) |
| `task-sot-missing/` | `--check-sot` FAIL (SOT READY claimed, no plugins) |
| `task-sot-mutated/` | `--check-sot` FAIL (working-tree file in mirror) |
| `task-sandbox-ok/` | `--check-sandbox` PASS (ports + runtime + compose) |
| `task-sandbox-no-plan/` | `--check-sandbox` FAIL (SANDBOX READY, no plan) |

Eval may also build ephemeral roots; these dirs prove claim theater vs green.
