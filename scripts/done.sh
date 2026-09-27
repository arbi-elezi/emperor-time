#!/usr/bin/env bash
# Thin twin: agent-defined DONE probes via Python core.
# Usage: done.sh <task-dir>
# Exit 0 only if every probe:/expect: pair in DONE.md matches.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
exec python3 "$ROOT/scripts/lib/done.py" "$@"
