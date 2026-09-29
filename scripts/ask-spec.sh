#!/usr/bin/env bash
# Thin twin: ask→spec HARD-GATE via Python core.
# Prints ASK-SPEC card, emits a scoped brief, or validates a task dir.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
exec python3 "$ROOT/scripts/lib/ask_spec.py" "$@"
