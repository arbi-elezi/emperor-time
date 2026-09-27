---
name: emperor-forge
description: >-
  Ship software: finish menu (merge locally / PR / keep), then public PR with
  consent when chosen. Use when tests pass, implementation is complete, user
  says finish, ship, PR, merge, or open a pull request. Refuses PR without
  EMPEROR_CONSENT_PR or a quoted yes.
license: MIT
metadata:
  version: 0.4.4
  part-of: emperor-time
---

# Emperor Forge — the software leaves the machine

Code that sits on a branch is not software. Software is merged or offered as a
PR the client can merge without babysitting comments.

## Before forge: finish menu

When implementation is complete (G4 PASS, suite green on this tree), do **not**
jump straight to a PR. Open `finish-menu.md` and/or run `scripts/emperor finish`:

1. Fresh suite on this tree (quote the tail).
2. Detect normal repo vs linked worktree vs detached HEAD.
3. Present the exact menu (3 options, or 2 if detached). Wait.
4. Execute the choice:
   - **Merge locally** → merge into confirmed base, re-verify, cleanup owned worktree.
   - **Pull Request** → continue with forge steps below (consent still required).
   - **Keep as-is** → report path; stop.
5. Discard only if the client asks and types `discard`. Never offer it unprompted.

## Forge (option 2 — Push and create a Pull Request)

1. `scripts/emperor done <task-dir>` must exit 0. Quote the tail.
2. `scripts/emperor gate g5 <task-dir>` must exit 0.
3. Consent: ledger must contain a quoted client yes **or**
   `EMPEROR_CONSENT_PR=1`. Otherwise stop and ask.
4. Run `scripts/emperor forge <task-dir>`.
5. PR body is generated from G1 + DONE probes + out-of-scope. No essay.
6. After the URL is printed, keep the worktree for review feedback, then
   `scripts/emperor queue next` when the client is done with this task.

If `gh` is missing: print the exact commands for the client. Do not pretend
the PR exists.
