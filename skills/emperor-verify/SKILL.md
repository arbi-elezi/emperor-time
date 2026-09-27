---
name: emperor-verify
description: >-
  Emperor Time — VERIFY / review / critique. Claim audit, eight-count
  self-critique, isolated hetero-critique, request-review HARD-GATE, mechanical
  G4. Use when reviewing a diff, requesting code review, claiming tests pass,
  asking if it is done, or before commit/PR/deliver/merge.
license: MIT
metadata:
  version: 0.4.11
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

## Hard rules

1. Run `scripts/emperor review` → quote `REVIEW checklist=yes`. Advance with
   `scripts/emperor review --advance N N+1` (skips fail). Self-review skip →
   `scripts/emperor review --reject-self-review` (HARD-GATE exit 1).
2. Read `chains/judgment-chain/SKILL.md` and select **one** aspect:
   `claim-audit.md` | `self-critique.md` | `hetero-critique.md` |
   `gatekeeping.md` | `verdicts-and-breaches.md`.
3. Claim ledger: every VERIFIED row needs quoted evidence. Cross-agent rows
   start CONJECTURE.
4. Self-critique uses `templates/critique.md`. "No findings" without named
   commands/paths is a fail.
5. Hetero-critique: run `scripts/review-pack.sh <task-dir> <base> <head>` and
   dispatch the pack to a **different** context (Steal Chain worker or a fresh
   subagent). The builder does not write the hetero verdict.
6. Act on Critical immediately; Important before proceed; Minor noted; pushback
   only with quoted evidence.
7. Run `scripts/gate.sh g4 <task-dir>` and quote the tail.
8. Deliver only after `scripts/gate.sh g5 <task-dir>`.
