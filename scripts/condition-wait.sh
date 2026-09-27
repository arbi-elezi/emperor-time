#!/usr/bin/env bash
# Thin twin: condition-based-waiting HARD-GATE card via Python core.
# Prints WAIT / COND / MUST lines. Does not mutate.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
exec python3 "$ROOT/scripts/lib/condition_wait.py" "$@"
