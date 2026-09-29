# state-hint-bind fixtures

Prove ask→spec STATE.md / state.md hint HARD-GATE
(`ask_spec.py --reject-over-state-class` / `--check-state-hints`).

PLAN_HINT_BIND binds PLAN.md / FINDINGS.md / PROGRESS.md. State-hint
bind closes the remaining bypass: park tiny-hint language ("fix typo" /
"one-line" / wording / trivial / nit / changelog only) in STATE.md
(resume disk from templates/STATE.md) while ask-spec+ledger+notes+plan
stay clean so FORCE_TABLE[large] / EFFORT_CAPS[large] unlock while
PLAN_HINT_BIND stays green. Harness owns force — agent does not inflate
class by editing STATE.md.

Length-only infer stays advisory. Only strong `_TINY_HINTS` bind.
`_LARGE_HINTS` lift the ceiling. Tighter-than-hint class remains OK.
Rejected: binding noisy `_SMALL_HINTS` (HARD-GATE/fixture/patch).

| Fixture | Expect |
|---|---|
| `task-state-park/` | FAIL — STATE.md tiny hints, ask-spec+ledger+notes+PLAN clean, effort_class:large |
| `task-clean/` | PASS — tiny-hint state corpus + effort_class:tiny |
| `task-tighter/` | PASS — no tiny hints; medium class unbound |
| `task-vacuous/` | `--check-state-hints` SKIP vacuous (no ask→spec) |

Honesty: `--check-plan-hints` may PASS on state-park (plan corpus clean)
while `--check-state-hints` FAILS — distinct from PLAN_HINT_BIND.
Iron: `STATE_HINT_BIND` (alongside `PLAN_HINT_BIND` / `NOTES_HINT_BIND` /
`TASK_HINT_BIND` / `BODY_HINT_BIND` / `SCOPE_HINT_BIND` / `SPEC_HINT_BIND` /
`ASK_HINT_BIND`).
G4 wires `_run_state_hints` after `_run_plan_hints`. v0.4.164.
