#!/usr/bin/env bash
# Detect git finish environment and print the integration menu.
# Does not merge, push, or delete. Agent + client choose; forge still needs consent.
set -euo pipefail

if ! git rev-parse --is-inside-work-tree >/dev/null 2>&1; then
  echo "FINISH FAIL: not a git repo" >&2
  exit 1
fi

GIT_DIR=$(cd "$(git rev-parse --git-dir)" && pwd -P)
GIT_COMMON=$(cd "$(git rev-parse --git-common-dir)" && pwd -P)
WORKTREE_PATH=$(git rev-parse --show-toplevel)
BRANCH=$(git branch --show-current || true)
HEAD_SHORT=$(git rev-parse --short HEAD)
SUPER=$(git rev-parse --show-superproject-working-tree 2>/dev/null || true)

kind="normal"
if [[ -n "$SUPER" ]]; then
  kind="normal"
elif [[ "$GIT_DIR" != "$GIT_COMMON" ]]; then
  if [[ -n "$BRANCH" ]]; then
    kind="worktree-named"
  else
    kind="worktree-detached"
  fi
fi

base_guess=""
if git rev-parse --verify origin/main >/dev/null 2>&1; then
  base_guess="main"
elif git rev-parse --verify origin/master >/dev/null 2>&1; then
  base_guess="master"
elif git symbolic-ref -q refs/remotes/origin/HEAD >/dev/null 2>&1; then
  base_guess=$(git symbolic-ref -q refs/remotes/origin/HEAD | sed 's@^refs/remotes/origin/@@')
fi
base_guess=${base_guess:-main}

echo "ENV kind=$kind"
echo "ENV branch=${BRANCH:-DETACHED}"
echo "ENV head=$HEAD_SHORT"
echo "ENV worktree=$WORKTREE_PATH"
echo "ENV base_guess=$base_guess"
if [[ "$kind" == worktree-* ]]; then
  if [[ "$WORKTREE_PATH" == */.worktrees/* || "$WORKTREE_PATH" == */worktrees/* ]]; then
    echo "ENV cleanup_owned=yes"
  else
    echo "ENV cleanup_owned=no"
  fi
else
  echo "ENV cleanup_owned=no"
fi

echo
if [[ "$kind" == "worktree-detached" ]]; then
  echo "MENU detached"
  cat <<MENU
Implementation complete. You're on a detached HEAD (externally managed workspace).

1. Push as new branch and create a Pull Request
2. Keep as-is (I'll handle it later)

Which option?
MENU
else
  echo "MENU standard"
  cat <<MENU
Implementation complete. What would you like to do?

1. Merge back to ${base_guess} locally
2. Push and create a Pull Request
3. Keep the branch as-is (I'll handle it later)

Which option?
MENU
fi
