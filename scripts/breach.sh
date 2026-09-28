#!/usr/bin/env bash
# Alias twin: breach → verdict Python core (hidden-breach HARD-GATE).
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
exec bash "$ROOT/scripts/verdict.sh" "$@"
