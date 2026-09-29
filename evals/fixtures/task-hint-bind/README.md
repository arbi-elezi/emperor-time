# task-hint-bind fixtures

Prove ask→spec task-dir corpus hint HARD-GATE
(`ask_spec.py --reject-over-task-class` / `--check-task-hints`).

BODY_HINT_BIND binds the ask→spec file alone. Task-hint bind closes the
remaining bypass: park tiny-hint language ("fix typo" / "one-line") in
ledger.md / work-order.md / brief.md / claims.md while ask-spec.md
(including ## Notes) stays clean so FORCE_TABLE[large] / EFFORT_CAPS[large]
unlock while BODY_HINT_BIND stays green. Harness owns force — agent does
not inflate class by editing sibling task files.

Length-only infer stays advisory. Only strong `_TINY_HINTS` bind.
`_LARGE_HINTS` lift the ceiling. Tighter-than-hint class remains OK.
Rejected: binding noisy `_SMALL_HINTS` (HARD-GATE/fixture/patch).

| Fixture | Expect |
|---|---|
| `task-ledger-park/` | FAIL — ledger tiny hints, ask-spec body clean, effort_class:large |
| `task-clean/` | PASS — tiny-hint corpus + effort_class:tiny |
| `task-tighter/` | PASS — no tiny hints; medium class unbound |
| `task-vacuous/` | `--check-task-hints` SKIP vacuous (no ask→spec) |

Honesty: `--check-body-hints` may PASS on ledger-park (ask-spec body clean)
while `--check-task-hints` FAILS — distinct from BODY_HINT_BIND.
Iron: `TASK_HINT_BIND` (alongside `BODY_HINT_BIND` / `SCOPE_HINT_BIND` /
`SPEC_HINT_BIND` / `ASK_HINT_BIND`).
G4 wires `_run_task_hints` after `_run_body_hints`. v0.4.161.
