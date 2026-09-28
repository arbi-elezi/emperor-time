#!/usr/bin/env bash
# Thin twin: task-done via Python core.
# Usage: task-done.sh [args...]
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
exec python3 "$ROOT/scripts/lib/task_done.py" "$@"
