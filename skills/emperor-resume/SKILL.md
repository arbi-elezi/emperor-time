---
name: emperor-resume
description: >-
  Resume from disk instead of restating the session. Use at session start,
  after compaction, or when the user says continue, resume, where were we.
  Planning-with-files pattern: PLAN.md FINDINGS.md PROGRESS.md.
license: MIT
metadata:
  version: 0.4.0
  part-of: emperor-time
---

# Emperor Resume

1. Read `.emperor/state.md` if it exists. Then the latest
   `.emperor/tasks/<id>/{PROGRESS,PLAN,FINDINGS,DONE,ledger}.md`.
2. Do not recap what those files already say. One line: current gate + blocker.
3. If DONE.md exists and `scripts/emperor done` still fails, you are not done.
4. If DONE passes and no PR, open `skills/emperor-forge/SKILL.md`.
5. If nothing is in flight, open `skills/emperor-queue/SKILL.md`.
