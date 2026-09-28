#!/usr/bin/env bash
# Thin twin: sdd-workspace via Python core.
# Usage: sdd-workspace.sh [args...]
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
exec python3 "$ROOT/scripts/lib/sdd_workspace.py" "$@"
