#!/usr/bin/env bash
# Thin twin: Judgment self-critique eight-count HARD-GATE via Python core.
# Prints CRITIQUE card or validates a task dir / critique file.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
exec python3 "$ROOT/scripts/lib/critique.py" "$@"
