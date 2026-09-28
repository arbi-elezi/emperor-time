#!/usr/bin/env bash
# Thin twin: task-brief via Python core.
# Usage: task-brief.sh [args...]
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
exec python3 "$ROOT/scripts/lib/task_brief.py" "$@"
