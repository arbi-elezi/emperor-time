#!/usr/bin/env bash
# Alias twin: swarm-emulate → steal-flow Python core.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
exec bash "$ROOT/scripts/steal-flow.sh" "$@"
