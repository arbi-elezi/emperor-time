# plan-hint-bind fixtures

Prove ask→spec PLAN.md/FINDINGS.md/PROGRESS.md hint HARD-GATE
(`ask_spec.py --reject-over-plan-class` / `--check-plan-hints`).

NOTES_HINT_BIND binds notes.md. Plan-hint bind closes the remaining
bypass: park tiny-hint language ("fix typo" / "one-line" / wording /
trivial / nit / changelog only) in PLAN.md / FINDINGS.md / PROGRESS.md
(G2 resume artifacts from templates/plan-files.md) while
ask-spec+ledger+notes stay clean so FORCE_TABLE[large] /
EFFORT_CAPS[large] unlock while NOTES_HINT_BIND stays green. Harness
owns force — agent does not inflate class by editing PLAN.md.

Length-only infer stays advisory. Only strong `_TINY_HINTS` bind.
`_LARGE_HINTS` lift the ceiling. Tighter-than-hint class remains OK.
Rejected: binding noisy `_SMALL_HINTS` (HARD-GATE/fixture/patch).

| Fixture | Expect |
|---|---|
| `task-plan-park/` | FAIL — PLAN.md tiny hints, ask-spec+ledger+notes clean, effort_class:large |
| `task-clean/` | PASS — tiny-hint plan corpus + effort_class:tiny |
| `task-tighter/` | PASS — no tiny hints; medium class unbound |
| `task-vacuous/` | `--check-plan-hints` SKIP vacuous (no ask→spec) |

Honesty: `--check-notes-hints` may PASS on plan-park (notes corpus clean)
while `--check-plan-hints` FAILS — distinct from NOTES_HINT_BIND.
Iron: `PLAN_HINT_BIND` (alongside `NOTES_HINT_BIND` / `TASK_HINT_BIND` /
`BODY_HINT_BIND` / `SCOPE_HINT_BIND` / `SPEC_HINT_BIND` / `ASK_HINT_BIND`).
G4 wires `_run_plan_hints` after `_run_notes_hints`. v0.4.163.
