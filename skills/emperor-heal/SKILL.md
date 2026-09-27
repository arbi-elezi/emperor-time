---
name: emperor-heal
description: >-
  Emperor Time — HEAL / Holy Chain. Stop digging, run the four-phase debug
  checklist, reproduce, bisect, minimal heal, verify root cause. Use when
  tests go red, a regression appears, state is corrupted, or a gate was skipped.
license: MIT
metadata:
  version: 0.4.7
  chain: holy-chain
---

# Emperor Heal (Holy Chain wrapper)

## MUST — four-phase checklist first

Before proposing any fix, open `skills/emperor-heal/debug-four-phases.md`
(Chain Jail leaf from Superpowers `systematic-debugging` → **4-phase list only**)
and/or run `scripts/emperor heal` (prints the mechanical PHASE / MUST card).

No fixes without Phase 1 (root-cause investigation). Do not load whole
`systematic-debugging`; ET + Holy Chain orchestrate.

## Steps

1. Run `scripts/emperor heal` → quote `DEBUG four_phases=yes`. Advance phases
   with `scripts/emperor heal --advance N N+1` (skips fail).
2. Read `chains/holy-chain/SKILL.md` → one aspect
   (`triage.md` | `reproduce-and-bisect.md` | `heal-and-verify.md` |
   `process-healing.md`) matching the current phase (see leaf table).
3. Snapshot. Reproduce. One hypothesis per step. Prediction before probe.
4. Minimal heal. Verify the cause, not the symptom (verification triad).
5. Postmortem line on the ledger: BROKE / CAUSE / HEAL / CAUGHT-BY /
   WOULD-HAVE-CAUGHT-SOONER.
6. If the *process* broke, re-enter at the earliest unsatisfied gate.
