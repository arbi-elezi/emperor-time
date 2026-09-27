---
name: emperor-heal
description: >-
  Emperor Time — HEAL / Holy Chain. Stop digging, run the four-phase debug
  checklist, reproduce, bisect, minimal heal, verify root cause. Use when
  tests go red, a regression appears, state is corrupted, a gate was skipped,
  or you need to locate a harness session transcript before diagnosing,
  or diagnose why a session went wrong (intake + path:line citations).
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


## MUST — session-discovery before citing transcript history

When a diagnosis needs prior session history (or the partner names a session id /
path), open `skills/emperor-heal/session-discovery.md`
(Chain Jail leaf from Superpowers `diagnosing-superpowers` → **session-discovery
locate aspect only**) and/or run `scripts/emperor session-discovery` (prints the
mechanical SESSION / PATH / STATUS / MUST card).

No session claims without a VERIFIED path. Do not load whole
`diagnosing-superpowers`; ET + Holy Chain orchestrate.


## MUST — diagnosing intake + citation before analysis

When a partner wants to know why a session went wrong (or wants evidence for a
bug report), open `skills/emperor-heal/diagnosing.md`
(Chain Jail leaf from Superpowers `diagnosing-superpowers` → **citation iron
law + intake-before-analysis only**) and/or run `scripts/emperor diagnose`
(prints the mechanical DIAGNOSE / INTAKE / CITE / MUST card).

No findings without `path:line`. No analysis before partner intake. Do not load
whole `diagnosing-superpowers`; ET + Holy Chain orchestrate.

## Steps

1. Run `scripts/emperor heal` → quote `DEBUG four_phases=yes`. Advance phases
   with `scripts/emperor heal --advance N N+1` (skips fail).
2. When transcripts are needed, run `scripts/emperor session-discovery` →
   quote `SESSION checklist=yes` and a `PATH ... status=VERIFIED` line.
   Guessing a session → `scripts/emperor session-discovery --reject-guess`
   (HARD-GATE exit 1).
3. When diagnosing a session: run `scripts/emperor diagnose` → quote
   `DIAGNOSE checklist=yes`. Finish intake before analysis. Uncited finding →
   `scripts/emperor diagnose --reject-uncited`. Skip-intake →
   `--reject-skip-intake` (HARD-GATE exit 1).
4. Read `chains/holy-chain/SKILL.md` → one aspect
   (`triage.md` | `reproduce-and-bisect.md` | `heal-and-verify.md` |
   `process-healing.md`) matching the current phase (see leaf table).
5. Snapshot. Reproduce. One hypothesis per step. Prediction before probe.
6. Minimal heal. Verify the cause, not the symptom (verification triad).
7. Postmortem line on the ledger: BROKE / CAUSE / HEAL / CAUGHT-BY /
   WOULD-HAVE-CAUGHT-SOONER.
8. If the *process* broke, re-enter at the earliest unsatisfied gate.
