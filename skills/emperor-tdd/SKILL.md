---
name: emperor-tdd
description: >-
  Emperor Time TDD iron law. Use BEFORE writing or editing production code for
  a feature, bugfix, refactor, or behavior change. No production code without
  a failing probe first. Delete implementation written before the probe failed.
  Prediction is ledgered before the command. Complements scientific-method.md.
license: MIT
metadata:
  version: 0.4.9
  part-of: emperor-time
---

# TDD Iron Law (Emperor Time)

**NO PRODUCTION CODE WITHOUT A FAILING PROBE FIRST.**

This is Vow of Evidence applied to code. Superpowers names the same law.
Emperor Time is stricter on one point: the prediction is written in the claim
ledger *before* the command runs, and the fail/pass tails are quoted.

## MUST — red-green-refactor checklist first

Before any production code for a G1 criterion, open
`skills/emperor-tdd/red-green-refactor.md`
(Chain Jail leaf from Superpowers `test-driven-development` → **The Iron Law**
/ **Red-Green-Refactor** only)
and/or run `scripts/emperor tdd` (prints the mechanical TDD / STEP / MUST card).

No jumping to production code without Step 2 FAIL observed and quoted.
Do not load whole `test-driven-development`; ET + emperor-tdd orchestrate.

## Hard rules

1. Run `scripts/emperor tdd` → quote `TDD checklist=yes`. Advance steps with
   `scripts/emperor tdd --advance N N+1` (skips fail). Jumping to prod →
   `scripts/emperor tdd --reject-prod` (HARD-GATE exit 1).
2. Write the probe (test or command) that must fail if the change is absent.
3. Ledger a HYPOTHESIS row with the predicted signal.
4. Run it. Watch it FAIL. Quote the tail. If it passes, the probe is wrong — fix the probe, not the product.
5. Smallest change that makes that probe pass. Nothing else.
6. Run it. Watch it PASS. Quote the tail. Then run the project suite.
7. Refactor only while the probe stays green.
8. If you already wrote implementation first: **delete it**. Delete means delete.
   Replay steps 2–7. Keeping it "as reference" is a vow breach.

Trivial doc/typo tasks: the probe may be `grep` / render, not a unit test.
The law still holds: observe absence, then change, then observe presence.

Work-order Tasks already encode this as Expected: FAIL then Expected: PASS.
Follow that file. Do not invent a second sequence.
