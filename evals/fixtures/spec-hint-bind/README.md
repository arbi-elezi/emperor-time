# spec-hint-bind fixtures

Prove ask→spec goal/done-when hint-corpus HARD-GATE
(`ask_spec.py --reject-over-spec-class` / `--check-spec-hints`).

ASK_HINT_BIND binds Ask(quoted) alone (else goal+done-when). Spec-hint
bind closes the remaining bypass: park tiny-hint language ("fix typo" /
"one-line") in goal/done-when while Ask(quoted) stays clean so
FORCE_TABLE[large] / EFFORT_CAPS[large] unlock while ASK_HINT_BIND stays
green. Harness owns force — agent does not inflate class by editing goal.

Length-only infer stays advisory. Only strong `_TINY_HINTS` bind.
`_LARGE_HINTS` lift the ceiling. Tighter-than-hint class remains OK.
Rejected: binding noisy `_SMALL_HINTS` (HARD-GATE/fixture/patch).

| Fixture | Expect |
|---|---|
| `task-goal-park/` | FAIL — goal/done-when tiny hints, Ask(quoted) clean, effort_class:large |
| `task-clean/` | PASS — tiny-hint goal+ask, effort_class:tiny |
| `task-tighter/` | PASS — no tiny hints; medium class unbound |
| `task-vacuous/` | `--check-spec-hints` SKIP vacuous (no ask→spec) |

Honesty: `--check-ask-hints` may PASS on goal-park (quoted ask clean)
while `--check-spec-hints` FAILS — distinct from ASK_HINT_BIND.
Iron: `SPEC_HINT_BIND` (alongside `ASK_HINT_BIND` / `ASK_THEN_SPEC_BEFORE_SETUP`).
G4 wires `_run_spec_hints` after `_run_ask_hints`. v0.4.158.
