#!/usr/bin/env bash
# Thin twin: task-start via Python core.
# Usage: task-start.sh [args...]
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
exec python3 "$ROOT/scripts/lib/task_start.py" "$@"
