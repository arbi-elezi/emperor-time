# done-hint-bind fixtures

Prove ask→spec DONE.md hint HARD-GATE
(`ask_spec.py --reject-over-done-class` / `--check-done-hints`).

STATE_HINT_BIND binds STATE.md / state.md. Done-hint bind closes the
remaining bypass: park tiny-hint language ("fix typo" / "one-line" /
wording / trivial / nit / changelog only) in DONE.md (G1 done probes from
templates/DONE.md) while ask-spec+ledger+notes+plan+state stay clean so
FORCE_TABLE[large] / EFFORT_CAPS[large] unlock while STATE_HINT_BIND stays
green. Harness owns force — agent does not inflate class by editing DONE.md.

Length-only infer stays advisory. Only strong `_TINY_HINTS` bind.
`_LARGE_HINTS` lift the ceiling. Tighter-than-hint class remains OK.
Rejected: binding noisy `_SMALL_HINTS` (HARD-GATE/fixture/patch).

| Fixture | Expect |
|---|---|
| `task-done-park/` | FAIL — DONE.md tiny hints, ask-spec+ledger+notes+PLAN+STATE clean, effort_class:large |
| `task-clean/` | PASS — tiny-hint done corpus + effort_class:tiny |
| `task-tighter/` | PASS — no tiny hints; medium class unbound |
| `task-vacuous/` | `--check-done-hints` SKIP vacuous (no ask→spec) |

Honesty: `--check-state-hints` may PASS on done-park (state corpus clean)
while `--check-done-hints` FAILS — distinct from STATE_HINT_BIND.
Iron: `DONE_HINT_BIND` (alongside `STATE_HINT_BIND` / `PLAN_HINT_BIND` /
`NOTES_HINT_BIND` / `TASK_HINT_BIND` / `BODY_HINT_BIND` / `SCOPE_HINT_BIND` /
`SPEC_HINT_BIND` / `ASK_HINT_BIND`).
G4 wires `_run_done_hints` after `_run_state_hints`. v0.4.165.
