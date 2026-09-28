#!/usr/bin/env bash
# Alias twin: self-critique → critique Python core.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
exec bash "$ROOT/scripts/critique.sh" "$@"
