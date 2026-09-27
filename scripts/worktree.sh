#!/usr/bin/env bash
# Thin twin: isolated git worktree create via Python core.
# Usage: worktree.sh <id> [base]
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
exec python3 "$ROOT/scripts/lib/worktree.py" "$@"
