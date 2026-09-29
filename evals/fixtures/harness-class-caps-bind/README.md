# harness-class-caps-bind fixtures

Prove harness class Caps bind HARD-GATE
(`harness_plan.py --reject-over-class-caps` / `--check-class-caps`).

Ask-class bind closes plan.effort_class vs ask→spec. Class-tools bind closes
Tools/Optional/Forbidden rewrite against FORCE_TABLE. Plan-caps bind closes
effort-cycles vs plan Caps (tighter-than-class OK). Class-caps bind closes
the remaining bypass: rewrite plan Caps upward past EFFORT_CAPS[class]
(tiny verify:16) while class+tools stay green. Harness owns force budget —
agent does not inflate Caps by editing the plan.

| Fixture | Expect |
|---|---|
| `task-inflated/` | FAIL — tiny ask+tools, Caps verify:16 (> tiny table 2) |
| `task-tighter/` | PASS — Caps verify:1 (< tiny table; PLAN_CAPS_BIND owns) |
| `task-clean/` | PASS — Caps match EFFORT_CAPS[tiny] |
| `task-vacuous/` | `--check-class-caps` SKIP vacuous (no plan / idle) |

Honesty: `--check-caps` (PLAN_CAPS_BIND) may PASS on inflated Caps with
zero cycles, while `--check-class-caps` FAILS — distinct from PLAN_CAPS_BIND.
Iron: `CLASS_CAPS_BIND` (alongside `HARNESS_OWNS_TOOL_AND_FORCE` /
`FORBIDDEN_TOOLS_NEVER_RUN` / `ALLOWED_TOOLS_ONLY` / `PLAN_CAPS_BIND` /
`CLASS_TOOLS_BIND` / `ASK_CLASS_BIND`).
G4 wires `_run_harness_class_caps` after `_run_harness_ask_class`. v0.4.156.
