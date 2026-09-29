#!/usr/bin/env bash
# Thin twin: proportionality / anti-loop HARD-GATE via Python core.
# Prints PROPORTIONALITY card, records cycles, or validates caps.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
exec python3 "$ROOT/scripts/lib/proportionality.py" "$@"
