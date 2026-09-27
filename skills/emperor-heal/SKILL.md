---
name: emperor-heal
description: >-
  Emperor Time — HEAL / Holy Chain. Stop digging, run the four-phase debug
  checklist, reproduce, bisect, minimal heal, verify root cause. Use when
  tests go red, a regression appears, state is corrupted, a gate was skipped,
  or you need to locate a harness session transcript before diagnosing,
  or diagnose why a session went wrong (intake + path:line citations),
  or trace a deep-stack bug backward to its original trigger before fixing,
  or add multi-layer validation after a source fix so invalid data cannot recur,
  or replace arbitrary sleep/setTimeout waits with condition-based waiting for flaky tests,
  or find which test creates leftover files / shared-state pollution without guessing.
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



## MUST — root-cause tracing before symptom fixes

When a bug appears deep in the call stack (wrong cwd, empty path, bad value far
from entry), open `skills/emperor-heal/root-cause-tracing.md`
(Chain Jail leaf from Superpowers `systematic-debugging` → **Trace backward /
Fix at source only**) and/or run `scripts/emperor trace` (prints the mechanical
TRACE / STEP / MUST card).

No symptom-site patches without a backward chain to the original trigger. Do not
load whole `systematic-debugging`; ET + Holy Chain orchestrate.



## MUST — defense-in-depth after source fix

When a bug was caused by invalid data and the source is fixed, open
`skills/emperor-heal/defense-in-depth.md`
(Chain Jail leaf from Superpowers `systematic-debugging` → **Validate at every
layer / Four layers only**) and/or run `scripts/emperor defense` (prints the
mechanical DEFENSE / LAYER / MUST card).

No single-layer guard as the whole fix. Layers are additive after the source
fix. Do not load whole `systematic-debugging`; ET + Holy Chain orchestrate.



## MUST — condition-based waiting instead of arbitrary sleep

When a test or async path waits (flaky timeouts, sleep/setTimeout guesses), open
`skills/emperor-heal/condition-based-waiting.md`
(Chain Jail leaf from Superpowers `systematic-debugging` → **Wait for the actual
condition / not a guess about timing only**) and/or run `scripts/emperor wait`
(prints the mechanical WAIT / COND / MUST card).

No arbitrary sleep as the wait. Name the condition; always timeout. Do not load
whole `systematic-debugging`; ET + Holy Chain orchestrate.



## MUST — find the polluter instead of guessing

When leftover files or shared state break later tests, open
`skills/emperor-heal/find-polluter.md`
(Chain Jail leaf from Superpowers `systematic-debugging` → **Find which test
creates unwanted files/state / do not guess the polluter only**) and/or run
`scripts/emperor polluter` (prints the mechanical POLLUTER / STEP / MUST card).

No guessing which test polluted. Name the marker; run candidates one-by-one.
Do not load whole `systematic-debugging`; ET + Holy Chain orchestrate.

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
4. When the failure is deep in a call stack: run `scripts/emperor trace` → quote
   `TRACE checklist=yes`. Symptom-only patch →
   `scripts/emperor trace --reject-symptom-fix`. Untraced implement →
   `--reject-untraced` (HARD-GATE exit 1).
5. After a source fix for invalid data: run `scripts/emperor defense` → quote
   `DEFENSE checklist=yes`. Single-layer-only →
   `scripts/emperor defense --reject-single-layer`. Unlayered ship →
   `--reject-unlayered` (HARD-GATE exit 1).
6. When waits are flaky or use arbitrary sleep/setTimeout: run
   `scripts/emperor wait` → quote `WAIT checklist=yes`. Arbitrary sleep →
   `scripts/emperor wait --reject-sleep`. Wait without a named condition →
   `--reject-unguessed` (HARD-GATE exit 1).
7. When leftover files or shared state break later tests: run
   `scripts/emperor polluter` → quote `POLLUTER checklist=yes`. Guessing the
   polluter → `scripts/emperor polluter --reject-guess`. Ship without finding
   it → `--reject-unbisected` (HARD-GATE exit 1).
8. Read `chains/holy-chain/SKILL.md` → one aspect
   (`triage.md` | `reproduce-and-bisect.md` | `heal-and-verify.md` |
   `process-healing.md`) matching the current phase (see leaf table).
9. Snapshot. Reproduce. One hypothesis per step. Prediction before probe.
10. Minimal heal. Verify the cause, not the symptom (verification triad).
11. Postmortem line on the ledger: BROKE / CAUSE / HEAL / CAUGHT-BY /
   WOULD-HAVE-CAUGHT-SOONER.
12. If the *process* broke, re-enter at the earliest unsatisfied gate.
