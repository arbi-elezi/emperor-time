#!/usr/bin/env bash
# Thin twin: defense-in-depth HARD-GATE card via Python core.
# Prints DEFENSE / LAYER / MUST lines. Does not mutate.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
exec python3 "$ROOT/scripts/lib/defense.py" "$@"
