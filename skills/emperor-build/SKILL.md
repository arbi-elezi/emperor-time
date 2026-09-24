---
name: emperor-build
description: >-
  Emperor Time — BUILD. Smallest change that makes the work-order probe pass.
  Use when implementing, writing code, or executing a work-order task.
  Failing probe first. Tripwires observed before flags/APIs/paths are asserted.
license: MIT
metadata:
  version: 0.3.0
---

# Emperor Build (G3 wrapper)

1. Refuse to build if `scripts/gate.sh g2 <task-dir>` has not passed.
2. Open the **current work-order task only**. Do not reload sibling aspects.
3. Write / run the failing probe. Quote the FAIL tail. Prediction first
   (`references/scientific-method.md` at first claim).
4. Smallest change. Observe tripwires (`--help`, read the file) before using them.
5. Re-run the probe. Quote the PASS tail.
6. Log divergences from the work order; if design changed, re-open G2.
7. Run `scripts/gate.sh g3 <task-dir>`.
8. If enlisting another agent, stop and load `skills/emperor-dispatch/SKILL.md`.
9. If something broke, load `skills/emperor-heal/SKILL.md` (Holy Chain).
