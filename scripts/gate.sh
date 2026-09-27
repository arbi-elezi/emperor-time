#!/usr/bin/env bash
# Thin twin: mechanical gates G0–G5 via Python core.
# Law is Judgment Chain; exit code is the lock. Does not invent policy.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
exec python3 "$ROOT/scripts/lib/gate.py" "$@"
