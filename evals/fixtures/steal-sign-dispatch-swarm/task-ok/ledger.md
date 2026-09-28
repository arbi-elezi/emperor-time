# Task Ledger — steal-flow-ok

## G0
- Origin: eval fixture
- Task: prove steal sign-in/dispatch/swarm hard-gate accept path
- Steal: sign-in-handoff + dispatch + swarm-emulate

## Sign-in
NEEDS-SIGN-IN resolved.
SIGN-IN HANDOFF: codex — client completed 2026-09-29; verified: "codex login status" exit 0

## Dispatch
STEAL dispatched worker. Runs under .emperor/runs/demo/codex/.

## Swarm
swarm-emulate bound N=2
disjoint SCOPE lists (no shared writable file)
Collected swarm-1/ swarm-2/
synthesis note: I synthesized the swarm siblings myself.

## G4
- Verdict: PASS

CLAIM AUDIT: 2 rows — 1 VERIFIED / 0 REFUTED / 1 CONJECTURE-labeled / 0 UNVERIFIABLE-labeled; spot-checks: row 2 quoted

CONSENT: task steal-flow
  codex → characterization tests   (per-task approval, client msg "yes use codex")

## G1 Acceptance criteria
1. steal_flow exits 0

## Out of scope
- live auth
