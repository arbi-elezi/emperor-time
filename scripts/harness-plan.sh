#!/usr/bin/env bash
# Thin twin: harness tool+force planner via Python core.
# Prints HARNESS-PLAN card, emits a plan from effort_class, or validates a task dir.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
exec python3 "$ROOT/scripts/lib/harness_plan.py" "$@"
