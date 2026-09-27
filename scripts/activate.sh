#!/usr/bin/env bash
# Thin twin: SessionStart MUST-route activation via Python core.
# Prints ACTIVATION / MUST lines. Does not mutate the tree.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
exec python3 "$ROOT/scripts/lib/activate.py" "$@"
