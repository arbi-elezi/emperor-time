#!/usr/bin/env bash
# Thin twin: pressure/academic HARD-GATE card via Python core.
# Prints PRESSURE / CASE / MUST / ACADEMIC lines. Does not mutate.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
exec python3 "$ROOT/scripts/lib/pressure.py" "$@"
