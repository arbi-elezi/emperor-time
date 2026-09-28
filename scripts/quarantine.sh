#!/usr/bin/env bash
# Thin twin: Steal quarantine admission HARD-GATE via Python core.
# Prints QUARANTINE card or validates a task dir / admission file.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
exec python3 "$ROOT/scripts/lib/quarantine.py" "$@"
