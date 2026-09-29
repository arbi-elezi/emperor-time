# Harness plan

effort_class: tiny
owner: harness
iron: HARNESS_OWNS_TOOL_AND_FORCE

## Tools
- ask-spec
- harness-plan
- activate
- route
- gate
- done
- tdd
- work-order

## Optional
- finish
- proportionality

## Caps
- verify: 2
- critique: 2
- gate: 3
- total: 4

## Forbidden
- excavate
- sandbox
- sot
- steal-flow
- heal
- critique
- grill
- parallel
- subagent
- forge
- context-build
- triage
- reproduce
- process-heal
- pin-and-consent
- quarantine
- swarm-emulate
- review-pack

## Force
- proportionality: do-once; verify-at-scale for tiny ≈ 1–2 checks; no museum of gates for a 2-line change
- harness selects tools + caps from effort_class; agent does not invent 20 verifications for a tiny ask
