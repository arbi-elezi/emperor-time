#!/usr/bin/env bash
# Thin twin: language-agnostic artifact survey via Python core.
# Always exits 0. No preferred stack.
set -uo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
exec python3 "$ROOT/scripts/lib/identify.py" "$@"
