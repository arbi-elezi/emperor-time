#!/usr/bin/env bash
# Thin twin: Dowsing Chain Mode 2 via Python core.
# Usage: dowse.sh [--check-auth] [--skip-versions] [--as-json]
# READ-ONLY: no installs, no logins, no credential access.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
exec python3 "$ROOT/scripts/lib/dowse.py" "$@"
