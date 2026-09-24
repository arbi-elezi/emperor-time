#!/usr/bin/env bash
# Isolated worktree for one swarm worker. Usage: worktree.sh <id> [base]
set -euo pipefail
ID="${1:-}"; BASE="${2:-HEAD}"
[[ -n "$ID" ]] || { echo "usage: $0 <id> [base]" >&2; exit 2; }
git rev-parse --is-inside-work-tree >/dev/null 2>&1 || { echo "WORKTREE FAIL: not a git repo" >&2; exit 1; }
DIR=".worktrees/$ID"
BRANCH="emperor/$ID"
mkdir -p .worktrees
if [[ -d "$DIR" ]]; then
  echo "WORKTREE EXISTS: $DIR"
  echo "$DIR"
  exit 0
fi
git worktree add -B "$BRANCH" "$DIR" "$BASE"
echo "WORKTREE: $DIR"
