#!/usr/bin/env bash
# Thin twin: receiving-code-review / receive checklist via Python core.
# Prints RECEIVE / STEP / MUST lines. Does not mutate the tree.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
exec python3 "$ROOT/scripts/lib/receive.py" "$@"
