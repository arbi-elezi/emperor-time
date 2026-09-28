#!/usr/bin/env bash
# Thin twin: work-order plan header + Task-N structure via Python core.
# Prints WORK-ORDER-TASKS card or validates a path. Does not mutate the tree.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
exec python3 "$ROOT/scripts/lib/work_order.py" "$@"
