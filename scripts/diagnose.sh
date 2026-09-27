#!/usr/bin/env bash
# Thin twin: diagnosing HARD-GATE card via Python core.
# Prints DIAGNOSE / INTAKE / CITE / MUST lines. Does not mutate.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
exec python3 "$ROOT/scripts/lib/diagnose.py" "$@"
