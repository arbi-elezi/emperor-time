#!/usr/bin/env bash
# Thin twin: session-discovery locate card via Python core.
# Prints SESSION / PATH / STATUS / MUST lines. Read-only; does not mutate.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
exec python3 "$ROOT/scripts/lib/session_discovery.py" "$@"
