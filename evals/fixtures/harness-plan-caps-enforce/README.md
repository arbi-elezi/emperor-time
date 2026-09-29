# harness-plan-caps-enforce fixtures

Prove harness plan-caps enforcement HARD-GATE
(`harness_plan.py --reject-over-plan-caps` / `--check-caps`).

Proportionality owns the class-table ceiling (`EFFORT_CAPS[effort_class]`).
Plan Caps are a separate harness-owned budget written into harness-plan —
they may be tighter than the class table. After forbid + allowlist, a tiny
plan with `verify: 1` could still thrash to 2 verify cycles (class allows)
and finish green. G4 `--check-caps` closes that hole.

| Fixture | Expect |
|---|---|
| `task-over-caps/` | FAIL — plan Caps verify:1; effort-cycles verify:2 (class tiny would allow 2) |
| `task-clean/` | PASS — plan Caps honored (cycles under budget) |
| `task-vacuous/` | `--check-caps` SKIP vacuous (no plan / idle) |

Honesty: plan Caps alone (no cycle ledger) PASS as zeros-under-cap.
Class-table proportionality remains a separate G4 check.
Iron: `PLAN_CAPS_BIND` (alongside `HARNESS_OWNS_TOOL_AND_FORCE` /
`FORBIDDEN_TOOLS_NEVER_RUN` / `ALLOWED_TOOLS_ONLY`).
G4 wires `_run_harness_caps` after `_run_harness_allow`. v0.4.153.
