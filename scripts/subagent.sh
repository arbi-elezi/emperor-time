#!/usr/bin/env bash
# Thin twin: subagent-driven-development / subagent checklist via Python core.
# Prints SUBAGENT / STEP / MUST lines. Does not mutate the tree.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
exec python3 "$ROOT/scripts/lib/subagent.py" "$@"
