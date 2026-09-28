#!/usr/bin/env bash
# Thin twin: heal-and-verify triad + postmortem HARD-GATE via Python core.
# Prints HEAL-VERIFY card or validates a task dir / heal file.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
exec python3 "$ROOT/scripts/lib/heal_verify.py" "$@"
