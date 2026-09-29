# Harness plan

effort_class: small
owner: harness
iron: HARNESS_OWNS_TOOL_AND_FORCE

## Tools
- ask-spec
- harness-plan
- activate
- route
- gate
- work-order
- tdd
- proportionality
- done
- finish

## Optional
- critique
- claim-audit

## Caps
- verify: 4
- critique: 4
- gate: 6
- total: 10

## Forbidden
- excavate
- sandbox
- sot
- steal-flow
- swarm-emulate
- parallel
- heal
- triage
- reproduce
- process-heal

## Force
- proportionality: bounded patch; one critique pass max when optional
- harness selects tools + caps from effort_class; agent does not invent 20 verifications for a tiny ask
