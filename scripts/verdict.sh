#!/usr/bin/env bash
# Thin twin: Judgment verdict + Breach Register HARD-GATE via Python core.
# Prints VERDICT card or validates a task dir / ledger file.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
exec python3 "$ROOT/scripts/lib/verdict.py" "$@"
