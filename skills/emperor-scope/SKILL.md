---
name: emperor-scope
description: >-
  Emperor Time — SCOPE / take-the-task. Quote the client, surface ambiguity,
  dowse repo evidence, write G0+G1. Use when the ask is vague, the user says
  find work, scope this, take this task, or before any design. Loads Dowsing
  Chain, not a substitute for it.
license: MIT
metadata:
  version: 0.3.0
  chain: dowsing-chain
---

# Emperor Scope (Dowsing wrapper)

This skill does **not** replace Dowsing Chain. It is the phase trigger.

1. Read `chains/dowsing-chain/SKILL.md` (router only).
2. Select **one** aspect: `task-dowsing.md` | `system-dowsing.md` | `lie-detection.md`.
3. Quote the client verbatim into `.emperor/tasks/<id>/ledger.md` from `templates/task-ledger.md`.
4. Write checkable acceptance criteria and an out-of-scope list (G1).
5. Run `scripts/gate.sh g0 <task-dir>` then `scripts/gate.sh g1 <task-dir>`. Quote the tails.
6. If the client has not chosen among options, stop and ask — do not invent scope.

Invocation Ritual still applies: router → one aspect. Record the aspect path in the ledger.
