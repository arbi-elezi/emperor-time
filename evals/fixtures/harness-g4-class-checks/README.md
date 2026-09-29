# harness-g4-class-checks fixtures

Prove harness-driven G4 critique / claim-audit selection
(`harness_plan.g4_check_mode` / `HARNESS_DRIVES_G4_CHECKS`).

Harness owns which checks run from ask→spec `effort_class` → FORCE_TABLE
Tools/Optional/Forbidden. Closes the tiny catch-22: FORCE_TABLE[tiny]
forbids critique while G4 always required eight-count (and burning a
critique cycle on every check). Forbid/allow still own use FAIL when
markers appear; G4 must not force the museum.

| Fixture | Expect |
|---|---|
| `task-tiny-skip/` | SKIP — tiny plan forbids critique; no critique.md; `--check-critique` / `--check-audit` SKIP |
| `task-medium-missing/` | FAIL — medium plan Tools include critique; no critique.md |
| `task-medium-ok/` | PASS — medium plan + complete eight-count + CLAIM AUDIT |
| `task-small-optional-absent/` | SKIP — small Optional critique/claim-audit unused |
| `task-small-optional-bad/` | FAIL — small Optional critique present but incomplete eight-count |
| `task-no-plan/` | FAIL — no plan → legacy always-on eight-count without critique.md |

Honesty: `--check-forbidden` still FAILs when tiny has critique.md
(forbid owns use). G4 wires existing `_run_critique` / `_run_claim_audit`
(cores SKIP with exit 0). Iron: `HARNESS_DRIVES_G4_CHECKS`.
v0.4.166.
