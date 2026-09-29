# harness-class-tools-bind fixtures

Prove harness class-tools FORCE_TABLE bind HARD-GATE
(`harness_plan.py --reject-over-class-tools` / `--check-class-tools`).

Forbid / allowlist / plan-caps close *runtime* thrash after a plan is written.
Class-tools bind closes *plan rewrite* force-upgrade: a tiny plan that lists
`tdd`/`work-order` under Tools (or omits `excavate` from Forbidden) can no
longer finish green. Harness owns tool selection via FORCE_TABLE — agent
does not upgrade force by editing the plan markdown.

| Fixture | Expect |
|---|---|
| `task-inflated/` | FAIL — tiny plan Tools include tdd/work-order (not in FORCE_TABLE[tiny]) |
| `task-unforbid/` | FAIL — tiny plan Forbidden omits excavate (class ban must bind) |
| `task-clean/` | PASS — Tools∪Optional ⊆ FORCE_TABLE; Forbidden ⊇ class bans |
| `task-vacuous/` | `--check-class-tools` SKIP vacuous (no plan / idle) |

Honesty: allowlist may PASS on an inflated plan (tdd is listed under Tools)
while class-tools FAILS — distinct from ALLOWED_TOOLS_ONLY.
Iron: `CLASS_TOOLS_BIND` (alongside `HARNESS_OWNS_TOOL_AND_FORCE` /
`FORBIDDEN_TOOLS_NEVER_RUN` / `ALLOWED_TOOLS_ONLY` / `PLAN_CAPS_BIND`).
G4 wires `_run_harness_class_tools` after `_run_harness_caps`. v0.4.154.
