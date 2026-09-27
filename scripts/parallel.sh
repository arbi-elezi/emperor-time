#!/usr/bin/env bash
# Thin twin: dispatching-parallel-agents / parallel checklist via Python core.
# Prints PARALLEL / STEP / MUST lines. Does not mutate the tree.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
exec python3 "$ROOT/scripts/lib/parallel.py" "$@"
