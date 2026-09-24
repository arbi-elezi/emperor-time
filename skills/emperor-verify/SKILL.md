---
name: emperor-verify
description: >-
  Emperor Time — VERIFY / review / critique. Claim audit, eight-count
  self-critique, isolated hetero-critique, mechanical G4. Use when reviewing a
  diff, claiming tests pass, asking if it is done, or before commit/PR/deliver.
license: MIT
metadata:
  version: 0.3.0
  chain: judgment-chain
---

# Emperor Verify (Judgment wrapper)

1. Read `chains/judgment-chain/SKILL.md` and select **one** aspect:
   `claim-audit.md` | `self-critique.md` | `hetero-critique.md` |
   `gatekeeping.md` | `verdicts-and-breaches.md`.
2. Claim ledger: every VERIFIED row needs quoted evidence. Cross-agent rows
   start CONJECTURE.
3. Self-critique uses `templates/critique.md`. "No findings" without named
   commands/paths is a fail.
4. Hetero-critique: run `scripts/review-pack.sh <task-dir> <base> <head>` and
   dispatch the pack to a **different** context (Steal Chain worker or a fresh
   subagent). The builder does not write the hetero verdict.
5. Run `scripts/gate.sh g4 <task-dir>` and quote the tail.
6. Deliver only after `scripts/gate.sh g5 <task-dir>`.
