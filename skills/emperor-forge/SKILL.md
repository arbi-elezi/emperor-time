---
name: emperor-forge
description: >-
  Ship software: commit, public PR with consent, PR body that should need no
  review comments. Use when tests pass, user says PR, ship, open a pull
  request, merge. Refuses without EMPEROR_CONSENT_PR or a quoted yes.
license: MIT
metadata:
  version: 0.4.0
  part-of: emperor-time
---

# Emperor Forge — the software leaves the machine

Code that sits on a branch is not software. Software is merged or at least
offered as a PR the client can merge without babysitting comments.

1. `scripts/emperor done <task-dir>` must exit 0. Quote the tail.
2. `scripts/emperor gate g5 <task-dir>` must exit 0.
3. Consent: ledger must contain a quoted client yes **or**
   `EMPEROR_CONSENT_PR=1`. Otherwise stop and ask.
4. Run `scripts/emperor forge <task-dir>`.
5. PR body is generated from G1 + DONE probes + out-of-scope. No essay.
6. After the URL is printed, `scripts/emperor queue next`.

If `gh` is missing: print the exact commands for the client. Do not pretend
the PR exists.
