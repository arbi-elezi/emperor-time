# ask-hint-bind fixtures

Prove ask→spec hint-ceiling HARD-GATE
(`ask_spec.py --reject-over-ask-class` / `--check-ask-hints`).

Plan binds (ASK_CLASS_BIND / CLASS_TOOLS_BIND / CLASS_CAPS_BIND) close
rewrite theater *after* ask→spec is written. Ask-hint bind closes the
remaining bypass: write `effort_class: large` on a tiny-hint ask
("fix typo" / "one-line" / "wording") so FORCE_TABLE[large] and
EFFORT_CAPS[large] unlock while plan binds stay green. Harness owns
force — agent does not inflate class by editing the ask-spec.

Length-only infer stays advisory. Only strong `_TINY_HINTS` bind.
`_LARGE_HINTS` lift the ceiling. Tighter-than-hint class remains OK.

| Fixture | Expect |
|---|---|
| `task-inflated/` | FAIL — tiny-hint ask, effort_class:large |
| `task-clean/` | PASS — tiny-hint ask, effort_class:tiny |
| `task-tighter/` | PASS — no tiny hints; medium class unbound |
| `task-vacuous/` | `--check-ask-hints` SKIP vacuous (no ask→spec) |

Honesty: `--check-ask-class` / `--check-class-caps` may PASS on inflated
ask-class (plan matches ask large) while `--check-ask-hints` FAILS —
distinct from ASK_CLASS_BIND / CLASS_CAPS_BIND.
Iron: `ASK_HINT_BIND` (alongside `ASK_THEN_SPEC_BEFORE_SETUP` /
`ASK_CLASS_BIND` / `CLASS_CAPS_BIND`).
G4 wires `_run_ask_hints` after `_run_harness_class_caps`. v0.4.157.
