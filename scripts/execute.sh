#!/usr/bin/env bash
# Thin twin: executing-plans / execute checklist via Python core.
# Prints EXECUTE / STEP / MUST lines. Does not mutate the tree.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
exec python3 "$ROOT/scripts/lib/execute.py" "$@"
