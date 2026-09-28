# steal-sign-dispatch-swarm fixtures

Prove Steal sign-in / dispatch / swarm HARD-GATE
(`steal_flow.py --reject-no-signin` / `--reject-no-dispatch-layout` /
`--reject-unbounded-swarm` / `--check-signin` / `--check-dispatch` /
`--check-swarm`).

| Fixture | Expect |
|---|---|
| `signin-ok.md` | PASS — SIGN-IN HANDOFF + client completed + verified |
| `signin-missing.md` | FAIL — NEEDS-SIGN-IN, no handoff |
| `signin-credentials.md` | FAIL — credential/token-shaped material in handoff |
| `dispatch-ok.md` | PASS (ledger-level) — layout + OBJECTIVE/SCOPE named |
| `dispatch-bad.md` | FAIL — dispatch claimed, no layout |
| `swarm-ok.md` | PASS — bound N, disjoint SCOPE, synthesis |
| `swarm-unbounded.md` | FAIL — N=8 / unbounded |
| `vacuous.md` | PASS vacuous — no steal-flow signals |
| `task-ok/` | PASS — handoff + runs layout + bounded swarm |
| `task-missing-signin/` | FAIL — sign-in claimed, no handoff |
| `task-bad-dispatch/` | FAIL — incomplete runs layout |
| `task-unbounded-swarm/` | FAIL — 5 swarm dirs / N>4 |
| `task-vacuous/` | PASS vacuous |
