# critique-eight-count-floor fixtures

Prove `critique.scale_with_effort` / `critique.require_eight_count_at` fold into
`harness_plan.g4_check_mode` (real bite, not schema theater).

Default floor remains **medium** (FORCE_TABLE medium Tools → require). These
fixtures override per-task `.emperor/config.yaml` so the knobs change G4
`--check-critique` outcomes.

| Fixture | Config | Expect |
|---|---|---|
| `task-medium-floor-large/` | scale=true, floor=large | SKIP — medium Tools critique below floor |
| `task-small-floor-small/` | scale=true, floor=small | FAIL — small Optional promoted to require; no critique.md |
| `task-medium-scale-off/` | scale=false, floor=large | FAIL — floor ignored; FORCE_TABLE medium still requires |

Iron: `HARNESS_DRIVES_G4_CHECKS` still owns forbidden→SKIP (tiny catch-22 closed).
Freeze `*-hint-bind`. No museum/Nen/k8s/embeddings. Local eval only.
v0.4.173.
