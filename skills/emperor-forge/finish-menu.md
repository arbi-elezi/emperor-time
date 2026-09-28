# Finish menu — integrate after green tests

**Provenance (aspect, not whole skill):**
- source: https://github.com/obra/superpowers/blob/main/skills/finishing-a-development-branch/SKILL.md
- heading: Present Options + Cleanup Workspace (adapted)
- license: MIT
- issue-context: forge assumed PR-only; missing client menu for local merge / keep / worktree cleanup

**Contract:** after G4 PASS and the project's suite is green on *this* tree, detect
the git environment, present the integration menu, wait for the client's choice,
then execute. Option 2 hands to forge (consent still required). Emperor Time
stays the orchestrator; do not announce a foreign skill name.

## Step 1 — Fresh suite on this tree

**HARD-GATE:** `scripts/lib/finish.py` refuses menu advance / done without a
green suite (`--reject-red-suite` always fails; `--require-green <task-dir>`
runs `done.py` probes — and/or `eval.py` when present/`--with-eval` — and
prints ENV/MENU only when green). Menu-only finish is soft theater.

Run the project's full test command on the tree you are about to integrate.
Prefer `scripts/emperor finish --require-green <task-dir>` (DONE probes via
`done.py`). Quote the tail. A green run earlier in the session does not count
(Vow of Evidence). If red: report failures and stop. No menu until green.

## Step 2 — Detect environment

Capture *before* any `cd` that leaves a worktree:

```bash
GIT_DIR=$(cd "$(git rev-parse --git-dir)" 2>/dev/null && pwd -P)
GIT_COMMON=$(cd "$(git rev-parse --git-common-dir)" 2>/dev/null && pwd -P)
WORKTREE_PATH=$(git rev-parse --show-toplevel)
BRANCH=$(git branch --show-current)
```

Or: `scripts/emperor finish` (Python core `scripts/lib/finish.py`; thin `finish.sh` / `finish.ps1` — prints `ENV` / `MENU` / options).

| State | Menu | Cleanup after local merge |
|---|---|---|
| `GIT_DIR == GIT_COMMON` (normal repo) | 3 options | none |
| linked worktree, named branch | 3 options | remove only if path under `.worktrees/` or `worktrees/` |
| linked worktree, detached HEAD | 2 options (no local merge) | leave in place (host-owned) |

Submodule guard: if `git rev-parse --show-superproject-working-tree` returns a
path, treat as normal repo (not a linked worktree).

## Step 3 — Base branch

Guess from plan, ledger, or upstream. Confirm with the client before a local
merge. Wrong-base merges are expensive to undo.

## Step 4 — Present exactly one menu

**Normal repo or named-branch worktree:**

```
Implementation complete. What would you like to do?

1. Merge back to <base-branch> locally
2. Push and create a Pull Request
3. Keep the branch as-is (I'll handle it later)

Which option?
```

**Detached HEAD:**

```
Implementation complete. You're on a detached HEAD (externally managed workspace).

1. Push as new branch and create a Pull Request
2. Keep as-is (I'll handle it later)

Which option?
```

Wait. Do not assume they want a PR. Discard is **not** on the menu; it exists
only if the client asks to throw the work away (see below).

## Step 5 — Execute

### 1 — Merge locally

From the main repo root (`git -C "$(git rev-parse --git-common-dir)/.." rev-parse --show-toplevel`):

1. `git checkout <base-branch> && git pull` (if remote tracking exists)
2. `git merge <feature-branch>`
3. Re-run the suite on the merged result. If red: stop, leave worktree/branch,
   investigate (Holy Chain). Nothing has been pushed.
4. On green: cleanup worktree (Step 6), then `git branch -d <feature-branch>`

### 2 — Push and create PR

`git push -u origin <feature-branch>` (detached: `git push origin HEAD:refs/heads/<new-branch>`).
Then forge: consent + `scripts/emperor forge <task-dir>`. Keep the worktree for
PR feedback.

### 3 — Keep as-is

Report branch name and worktree path. No cleanup.

### Discard (only on explicit client request)

Confirm with the exact word `discard` after listing branch, commits, and
worktree path. Then cleanup (Step 6) and `git branch -D <feature-branch>`.
Never offer discard unprompted. Never `--force` worktree removal on your own.

## Step 6 — Worktree cleanup

Runs for local merge and confirmed discard only. Options 2 and 3 preserve the
worktree. Always `cd` to main repo root first.

- `GIT_DIR == GIT_COMMON`: nothing to remove.
- `WORKTREE_PATH` under `.worktrees/` or `worktrees/`: `git worktree remove` then
  `git worktree prune`. If remove refuses (modified/untracked): show
  `git -C "$WORKTREE_PATH" status --porcelain -uall` and ask commit / move /
  delete. Never `--force` without that choice.
- Otherwise: host-owned workspace; leave it.

## Rationalizations (stop)

| Excuse | Reality |
|---|---|
| Tests passed earlier | Re-run on the tree you integrate |
| They obviously want a PR | Present the menu; wait |
| Offer discard because they seem done | Discard only when they ask |
| "yeah get rid of it" is enough | Only the typed word `discard` |
| PR is up, delete the worktree | Keep it for review feedback |
| Removal refused → `--force` | Ask; uncommitted files may exist only there |
| Base is obviously main | Confirm fork point |
