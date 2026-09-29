# harness-ask-class-bind fixtures

Prove harness ask→spec effort_class bind HARD-GATE
(`harness_plan.py --reject-class-mismatch` / `--check-ask-class`).

Class-tools bind closes plan Tools/Optional/Forbidden rewrite against
FORCE_TABLE[plan.effort_class]. Ask-class bind closes the remaining
bypass: rewrite plan `effort_class` tiny→large (with matching large
Tools/Forbidden) so CLASS_TOOLS_BIND stays green while ask→spec stayed
tiny. Harness owns class — agent does not upgrade force by editing the
plan class line.

| Fixture | Expect |
|---|---|
| `task-mismatch/` | FAIL — ask→spec tiny, plan large (FORCE_TABLE[large] shape) |
| `task-clean/` | PASS — plan.effort_class matches ask→spec |
| `task-vacuous/` | `--check-ask-class` SKIP vacuous (no plan / idle) |

Honesty: class-tools may PASS on a mismatch plan (valid FORCE_TABLE[large])
while ask-class FAILS — distinct from CLASS_TOOLS_BIND.
Iron: `ASK_CLASS_BIND` (alongside `HARNESS_OWNS_TOOL_AND_FORCE` /
`FORBIDDEN_TOOLS_NEVER_RUN` / `ALLOWED_TOOLS_ONLY` / `PLAN_CAPS_BIND` /
`CLASS_TOOLS_BIND`).
G4 wires `_run_harness_ask_class` after `_run_harness_class_tools`. v0.4.155.
