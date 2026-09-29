# Gates map (operator)

Load on demand. Full table: `references/mechanical-gates.md`.

| Gate | Script | Little-ask note |
|---|---|---|
| G0 | `emperor gate g0` | **never skip** ask→spec + harness-plan |
| G1 | `emperor gate g1` | acceptance criteria |
| G2 | `emperor gate g2` | work-order when non-trivial |
| G3 | `emperor gate g3` | impact map vs diff |
| G4 | `emperor gate g4` | class-scaled; iron consent always |
| G5 | `emperor gate g5` | verdict; forge consent if PR |

## Always hard (config `gates.always_hard`)

forge-pr-consent · pin-and-consent · quarantine · steal-consent · secrets-no-leak

## Tiny may SKIP (activity / harness-driven)

Critique museum, excavate, sandbox up, hetero review-pack — when forbidden/unlisted by harness plan (`HARNESS_DRIVES_G4_CHECKS`).

## Never soft on tiny

Ask→spec emit, harness-plan emit, iron consent family, DONE probes when claiming done.
