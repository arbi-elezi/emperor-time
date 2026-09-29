# harness-verdict-cites fixtures

Prove harness-driven G5 verdict citations
(`verdict.py` + `harness_plan.g4_check_mode` / `HARNESS_DRIVES_G4_CHECKS`).

After v0.4.166 G4 critique/claim-audit SKIP when tiny forbids those tools,
G5 still forced the citation museum parenthetical
`(claim audit: …; critique: …; hetero: …)` — including `absent` theater —
or allowed `critique: absent` while medium Tools *require* critique.

Harness owns which citations are required:

| Fixture | Expect |
|---|---|
| `task-tiny-bare/` | PASS — tiny forbids critique/review-pack; unlists claim-audit; bare `Verdict: PASS` OK |
| `task-medium-absent/` | FAIL — medium Tools require critique/claim-audit/review-pack; `*: absent` refused |
| `task-medium-ok/` | PASS — medium + real artifact cites |
| `task-no-plan-bare/` | FAIL — no plan → legacy always-on cite fields |
| `task-no-plan-ok/` | PASS — no plan + legacy cites (`hetero: absent` still OK) |

Iron: `HARNESS_DRIVES_G4_CHECKS` (same drive: which checks / how many / which cites).
v0.4.167.
