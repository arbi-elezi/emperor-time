#!/usr/bin/env bash
# Thin twin: find-polluter HARD-GATE card via Python core.
# Prints POLLUTER / STEP / MUST lines. Does not mutate.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
exec python3 "$ROOT/scripts/lib/polluter.py" "$@"
