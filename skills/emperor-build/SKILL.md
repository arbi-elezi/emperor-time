---
name: emperor-build
description: >-
  Emperor Time — BUILD. Smallest change that makes the work-order probe pass.
  Use when implementing, writing code, or executing a work-order task.
  Failing probe first. Tripwires observed before flags/APIs/paths are asserted.
license: MIT
metadata:
  version: 0.4.10
  part-of: emperor-time
---

# Emperor Build (G3 wrapper)

1. Refuse to build if `scripts/gate.sh g2 <task-dir>` has not passed.
2. For standard/heavy tasks: open `skills/emperor-worktree/isolation-checklist.md`
   and/or run `scripts/emperor iso` before mutating the client's checkout.
   Trivial tasks may skip with `worktree: skipped (trivial)` ledgered.
3. Open the **current work-order task only**. Do not reload sibling aspects.
4. Open `skills/emperor-tdd/red-green-refactor.md` and/or run `scripts/emperor tdd`
   (TDD / STEP / MUST card). Write / run the failing probe. Quote the FAIL
   tail. Prediction first (`references/scientific-method.md` at first claim).
5. Smallest change. Observe tripwires (`--help`, read the file) before using them.
6. Re-run the probe. Quote the PASS tail.
7. Log divergences from the work order; if design changed, re-open G2.
8. Run `scripts/gate.sh g3 <task-dir>`.
9. If enlisting another agent, stop and load `skills/emperor-dispatch/SKILL.md`.
10. If something broke, load `skills/emperor-heal/SKILL.md` (Holy Chain).
