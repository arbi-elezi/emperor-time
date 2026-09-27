#!/usr/bin/env bash
# Thin twin: grill/brainstorm checklist via Python core (require-design path).
# Prints GRILL / STEP / MUST lines. Does not mutate the tree.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
exec python3 "$ROOT/scripts/lib/grill.py" "$@"
