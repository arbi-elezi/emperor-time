---
name: emperor-tdd
description: >-
  Emperor Time TDD iron law. Use BEFORE writing or editing production code for
  a feature, bugfix, refactor, or behavior change. No production code without
  a failing probe first. Delete implementation written before the probe failed.
  Prediction is ledgered before the command. Complements scientific-method.md.
license: MIT
metadata:
  version: 0.3.2
  part-of: emperor-time
---

# TDD Iron Law (Emperor Time)

**NO PRODUCTION CODE WITHOUT A FAILING PROBE FIRST.**

This is Vow of Evidence applied to code. Superpowers names the same law.
Emperor Time is stricter on one point: the prediction is written in the claim
ledger *before* the command runs, and the fail/pass tails are quoted.

## Hard rules

1. Write the probe (test or command) that must fail if the change is absent.
2. Ledger a HYPOTHESIS row with the predicted signal.
3. Run it. Watch it FAIL. Quote the tail. If it passes, the probe is wrong — fix the probe, not the product.
4. Smallest change that makes that probe pass. Nothing else.
5. Run it. Watch it PASS. Quote the tail.
6. Refactor only while the probe stays green.
7. If you already wrote implementation first: **delete it**. Delete means delete.
   Replay steps 1–6. Keeping it "as reference" is a vow breach.

Trivial doc/typo tasks: the probe may be `grep` / render, not a unit test.
The law still holds: observe absence, then change, then observe presence.

Work-order Tasks already encode this as Expected: FAIL then Expected: PASS.
Follow that file. Do not invent a second sequence.
