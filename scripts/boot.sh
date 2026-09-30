#!/usr/bin/env bash
# Thin twin: silent session boot via Python core (host.env + survey + eval.log).
# User never types this. Exit 0 normally; exit 1 when ET-tree eval FAILED.
set -uo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
# Hint shell for host.py when /proc parent is ambiguous.
export EMPEROR_SHELL="${EMPEROR_SHELL:-bash}"
exec python3 "$ROOT/scripts/lib/boot.py" "$@"
