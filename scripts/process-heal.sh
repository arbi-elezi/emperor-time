#!/usr/bin/env bash
# Thin twin: holy process-healing register + re-entry HARD-GATE via Python core.
# Prints PROCESS-HEAL card or validates a task dir / process-heal file.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
exec python3 "$ROOT/scripts/lib/process_heal.py" "$@"
