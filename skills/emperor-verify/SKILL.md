---
name: emperor-verify
description: >-
  Emperor Time — VERIFY / review / critique. Claim audit, eight-count
  self-critique, isolated hetero-critique, request-review HARD-GATE,
  verification-before-completion / evidence HARD-GATE, mechanical G4. Use when
  reviewing a diff, requesting code review, claiming tests pass, saying done /
  fixed / green, or before commit/PR/deliver/merge.
license: MIT
metadata:
  version: 0.4.14
  part-of: emperor-time
  chain: judgment-chain
---

# Emperor Verify (Judgment wrapper)

## MUST — request-review checklist first

Before merge to main, after a major feature, and after each subagent-driven
task, open `skills/emperor-verify/request-review-checklist.md`
(Chain Jail leaf from Superpowers `requesting-code-review` → When / How /
Act-on-feedback only)
and/or run `scripts/emperor review` (prints the mechanical REVIEW / STEP / MUST
card).

No author self-review in place of dispatch. Do not load whole
`requesting-code-review`; ET + emperor-verify orchestrate.

## MUST — evidence checklist before completion claims

Before claiming tests pass, bug fixed, build green, requirements met, agent
done, or any satisfaction/completion phrasing — and before commit/PR/deliver —
open `skills/emperor-verify/verification-checklist.md`
(Chain Jail leaf from Superpowers `verification-before-completion` → The Iron
Law / The Gate Function only)
and/or run `scripts/emperor evidence` (prints the mechanical EVIDENCE / STEP /
MUST card).

No completion claim without a fresh proving command in this turn. Do not load
whole `verification-before-completion`; ET + emperor-verify orchestrate.

## Hard rules

1. Run `scripts/emperor evidence` → quote `EVIDENCE checklist=yes` before any
   completion / pass / fixed / done claim. Advance with
   `scripts/emperor evidence --advance N N+1` (skips fail). Unverified claim →
   `scripts/emperor evidence --reject-unverified` (HARD-GATE exit 1).
2. Run `scripts/emperor review` → quote `REVIEW checklist=yes`. Advance with
   `scripts/emperor review --advance N N+1` (skips fail). Self-review skip →
   `scripts/emperor review --reject-self-review` (HARD-GATE exit 1).
3. Read `chains/judgment-chain/SKILL.md` and select **one** aspect:
   `claim-audit.md` | `self-critique.md` | `hetero-critique.md` |
   `gatekeeping.md` | `verdicts-and-breaches.md`.
4. Claim ledger: every VERIFIED row needs quoted evidence. Cross-agent rows
   start CONJECTURE.
5. Self-critique uses `templates/critique.md`. "No findings" without named
   commands/paths is a fail.
6. Hetero-critique: run `scripts/review-pack.sh <task-dir> <base> <head>` and
   dispatch the pack to a **different** context (Steal Chain worker or a fresh
   subagent). The builder does not write the hetero verdict.
7. Act on Critical immediately; Important before proceed; Minor noted; pushback
   only with quoted evidence.
8. Run `scripts/gate.sh g4 <task-dir>` and quote the tail.
9. Deliver only after `scripts/gate.sh g5 <task-dir>`.
