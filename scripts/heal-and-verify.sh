#!/usr/bin/env bash
# Alias twin: heal-and-verify → heal_verify Python core.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
exec bash "$ROOT/scripts/heal-verify.sh" "$@"
