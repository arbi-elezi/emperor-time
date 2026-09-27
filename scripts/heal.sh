#!/usr/bin/env bash
# Thin twin: four-phase debug checklist via Python core (heal path).
# Prints DEBUG / PHASE / MUST lines. Does not mutate the tree.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
exec python3 "$ROOT/scripts/lib/debug_phases.py" "$@"
