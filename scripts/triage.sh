#!/usr/bin/env bash
# Thin twin: holy triage block + snapshot HARD-GATE via Python core.
# Prints TRIAGE card or validates a task dir / triage file.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
exec python3 "$ROOT/scripts/lib/triage.py" "$@"
