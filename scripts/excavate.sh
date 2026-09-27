#!/usr/bin/env bash
# Thin alias: same survey as identify. First-class excavate tool name.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")" && pwd)"
exec bash "$ROOT/identify.sh" "$@"
