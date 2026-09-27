#!/usr/bin/env bash
# Thin twin: root-cause tracing HARD-GATE card via Python core.
# Prints TRACE / STEP / MUST lines. Does not mutate.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
exec python3 "$ROOT/scripts/lib/root_cause.py" "$@"
