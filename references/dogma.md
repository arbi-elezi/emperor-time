# Dogma (the rite, not the paperwork)

Emperor Time is a dogma enforcer. Markdown is the missal. Hooks and scripts are
the Inquisition. If a rule exists only as a file nobody runs, it is not dogma.

## Primary law

The agent names DONE. The script tests DONE. The client does not babysit.

`.emperor/tasks/<id>/DONE.md` is written by the agent from G1 + observed stack.
`scripts/done.sh` executes the probes listed there. Exit 0 is DONE. A paragraph
that says "done" is heresy.

## No easy path

Convenience that skips a rite is a breach:

- ship without the FAIL-then-PASS tails
- "good enough" / TODO / skip the hard file
- steal a whole religion instead of the one heading
- mark VERIFIED from memory
- widen G1 after BUILD started without recording SCOPE-CREEP
- shrink G1 after a fail to make the gate open (scope drain)

Right-sizing a *trivial* task to one sentence per phase is still the rite.
Gold-plating beyond G1 is also heresy (Worthy Spend). Perfect means the rite
was kept, not that you built a cathedral.

## Self-inquisition

Before any non-trivial edit and before DONE:

1. Change rationale: why this file, why this hunk, which G1 line it serves.
2. Fact-check: observe the current text; do not edit a rumor.
3. Calibration: state p(this decision is wrong). If p ≥ 0.3, run one more
   probe or steal one aspect before committing the hunk.

## Swarm

If the host has native swarm (Kimi `/swarm`, UltraCode swarm), use it under
Steal consent and quarantine each worker. If not, `chains/steal-chain/swarm-emulate.md`.
Lack of a vendor button is not permission to go sequential on disjoint work.
