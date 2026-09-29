# harness-tool-force fixtures

Prove harness tool+force planner HARD-GATE (`harness_plan.py --reject-no-plan` /
`--require-plan` / `--check-harness-plan` / `--emit`).

Harness owns tool selection + proportionality of force from ask→spec
`effort_class` — not agent-facing CLI recall.

| Fixture | Expect |
|---|---|
| `task-ok/` | PASS — ask-spec tiny + harness-plan with few tools / low caps / forbidden heavy |
| `task-no-plan/` | FAIL — ask-spec present, no harness-plan (`--require-plan`) |
| `task-tiny-heavy/` | FAIL — tiny plan selects forbidden heavy tool (critique/excavate) |
| `task-vacuous/` | `--check-harness-plan` SKIP vacuous; `--require-plan` FAIL — no plan |
| `task-small-ok/` | PASS — small class plan with work-order/tdd tools, caps match table |

Honesty: idle paths SKIP; G0 `--require-plan` never vacuous. v0.4.150.
