#!/usr/bin/env bash
# Thin twin: adjustable-rigor config (schema v1) via Python core.
# show|get|set|edit — host-agnostic.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
exec python3 "$ROOT/scripts/lib/config.py" "$@"
