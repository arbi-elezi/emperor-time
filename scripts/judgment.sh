#!/usr/bin/env bash
# Thin twin: optional judgment adapter stub (soft None when off/unavailable).
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
exec python3 "$ROOT/scripts/lib/judgment.py" "$@"
