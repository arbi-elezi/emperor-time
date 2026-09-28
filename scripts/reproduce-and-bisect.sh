#!/usr/bin/env bash
# Alias twin: reproduce-and-bisect → reproduce Python core.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
exec bash "$ROOT/scripts/reproduce.sh" "$@"
