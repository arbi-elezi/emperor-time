#!/usr/bin/env bash
# Thin twin: Steal sign-in / dispatch / swarm HARD-GATE via Python core.
# Prints STEAL-FLOW card or validates a task dir.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
exec python3 "$ROOT/scripts/lib/steal_flow.py" "$@"
