#!/usr/bin/env bash
# Alias twin: process-healing → process-heal Python core.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
exec bash "$ROOT/scripts/process-heal.sh" "$@"
