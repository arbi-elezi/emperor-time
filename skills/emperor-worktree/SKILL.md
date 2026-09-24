---
name: emperor-worktree
description: >-
  Emperor Time worktree isolation. Use before standard or heavy BUILD so the
  client's current checkout stays clean. Create a git worktree, install deps,
  prove a green baseline, then implement the work-order there.
license: MIT
metadata:
  version: 0.3.2
  part-of: emperor-time
---

# Worktree isolation

Standard and heavy tasks do not mutate the client's dirty tree.

1. If already in a linked worktree (`git rev-parse --git-dir` != `--git-common-dir`), stay.
2. Else:
   ```bash
   mkdir -p .worktrees
   git worktree add .worktrees/<task-id> -b emperor/<task-id>
   ```
   Add `.worktrees/` to `.gitignore` if needed.
3. Install project deps in the worktree. Run the baseline suite. Quote the tail.
4. Implement only inside that worktree. Ledger the path.
5. Review pack diffs that worktree against the base branch SHA.
6. Merge/copy back only after G4 PASS.

Trivial tasks may stay on the current tree. Record `worktree: skipped (trivial)`.
