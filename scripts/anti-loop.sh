#!/usr/bin/env bash
# Alias twin: anti-loop → proportionality Python core.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
exec bash "$ROOT/scripts/proportionality.sh" "$@"
