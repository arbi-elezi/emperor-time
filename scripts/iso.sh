#!/usr/bin/env bash
# Thin twin: worktree isolation checklist via Python core (emperor-worktree path).
# Prints WORKTREE / STEP / MUST lines. Does not mutate the tree.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
exec python3 "$ROOT/scripts/lib/worktree_iso.py" "$@"
