# harness-forbid-enforce fixtures

Prove harness forbidden-tool enforcement HARD-GATE
(`harness_plan.py --reject-forbidden-used` / `--check-forbidden`).

Plan-without-enforcement is soft theater: a tiny plan can list critique/sandbox/
grill as forbidden, then still thrash those paths and pass G0 `--require-plan`.
G4 `--check-forbidden` closes that hole.

| Fixture | Expect |
|---|---|
| `task-forbidden-used/` | FAIL — tiny plan forbids critique; critique.md + effort-cycles critique>0 |
| `task-clean/` | PASS — tiny plan + allowed tools only (no forbidden markers) |
| `task-vacuous/` | `--check-forbidden` SKIP vacuous (no plan / idle) |

Honesty: plan file listing a tool under Forbidden is not itself "use".
Iron: `FORBIDDEN_TOOLS_NEVER_RUN` (alongside `HARNESS_OWNS_TOOL_AND_FORCE`).
G4 wires `_run_harness_forbid`. v0.4.151.
