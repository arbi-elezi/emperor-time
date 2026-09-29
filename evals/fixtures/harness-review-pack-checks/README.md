# harness-review-pack-checks fixtures

Prove harness-driven G4 review-pack isolation selection
(`harness_plan.g4_check_mode` / `HARNESS_DRIVES_G4_CHECKS`).

Harness owns whether `--check-isolation` requires an isolated pack from
ask→spec `effort_class` → FORCE_TABLE Tools/Optional/Forbidden. Closes the
medium hole left after v0.4.167: Tools list review-pack (and G5 requires a
hetero cite) while G4 always SKIP'd when the pack was absent — cite theater
without an examiner pack. Forbid/allow still own use FAIL when markers appear.

| Fixture | Expect |
|---|---|
| `task-tiny-skip/` | SKIP — tiny plan forbids review-pack; no pack |
| `task-medium-missing/` | FAIL — medium Tools require review-pack; no pack |
| `task-medium-ok/` | PASS — medium plan + clean `review-pack/` |
| `task-medium-dirty/` | FAIL — medium plan + author-diary file in pack |
| `task-no-plan-vacuous/` | SKIP — no plan → legacy idle (no pack / no hetero) |
| `task-no-plan-signal/` | FAIL — no plan → legacy always activity; hetero claimed, pack absent |

Honesty: `--check-forbidden` still FAILs when tiny has `review-pack/`
(forbid owns use). G4 wires existing `_run_review_isolation` (core SKIPs with
exit 0). Iron: `HARNESS_DRIVES_G4_CHECKS`.
v0.4.168.
