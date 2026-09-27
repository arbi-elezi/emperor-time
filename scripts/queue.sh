#!/usr/bin/env bash
# Thin twin: local / GitHub / Linear work picker via Python core.
# Kanban WIP=1 — see scripts/lib/queue.py
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
exec python3 "$ROOT/scripts/lib/queue.py" "$@"
