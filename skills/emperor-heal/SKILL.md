---
name: emperor-heal
description: >-
  Emperor Time — HEAL / Holy Chain. Stop digging, reproduce, bisect, minimal
  heal, verify root cause. Use when tests go red, a regression appears, state
  is corrupted, or a gate was skipped.
license: MIT
metadata:
  version: 0.3.0
  chain: holy-chain
---

# Emperor Heal (Holy Chain wrapper)

1. Read `chains/holy-chain/SKILL.md` → one aspect
   (`triage.md` | `reproduce-and-bisect.md` | `heal-and-verify.md` |
   `process-healing.md`).
2. Snapshot. Reproduce. One hypothesis per step. Prediction before probe.
3. Minimal heal. Verify the cause, not the symptom.
4. Postmortem line on the ledger: BROKE / CAUSE / HEAL / CAUGHT-BY /
   WOULD-HAVE-CAUGHT-SOONER.
5. If the *process* broke, re-enter at the earliest unsatisfied gate.
