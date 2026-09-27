#!/usr/bin/env bash
# Thin twin: skill-discovery (SDO) HARD-GATE card via Python core.
# Prints SDO / PRIN / GATE / MUST lines. Does not mutate.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
exec python3 "$ROOT/scripts/lib/sdo.py" "$@"
