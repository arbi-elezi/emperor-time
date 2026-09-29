# harness-allowlist-enforce fixtures

Prove harness allowlist enforcement HARD-GATE
(`harness_plan.py --reject-extra-tools` / `--check-allowed`).

Forbid-enforce owns named Forbidden bans. Allowlist owns the gap: tools that
are neither in Tools∪Optional nor Forbidden (e.g. tdd / work-order / diagnose
on a tiny plan) could still thrash and finish green. G4 `--check-allowed`
closes that hole.

| Fixture | Expect |
|---|---|
| `task-extra-used/` | FAIL — tiny plan; tdd.md present (tdd not in Tools/Optional/Forbidden) |
| `task-clean/` | PASS — tiny plan + allowed tools only (no extra markers) |
| `task-vacuous/` | `--check-allowed` SKIP vacuous (no plan / idle) |

Honesty: Tools/Optional/Forbidden lists in the plan file are not themselves
"use". Forbidden-used stays under `--check-forbidden` (sharper card).
Iron: `ALLOWED_TOOLS_ONLY` (alongside `HARNESS_OWNS_TOOL_AND_FORCE` /
`FORBIDDEN_TOOLS_NEVER_RUN`).
G4 wires `_run_harness_allow` after `_run_harness_forbid`. v0.4.152.
