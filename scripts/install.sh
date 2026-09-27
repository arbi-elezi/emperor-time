#!/usr/bin/env bash
# Thin twin: deploy Emperor Time into a harness skill directory via Python core.
# Usage: install.sh <harness> [scope] [project-path] [--with-chain-skills] [--dry-run]
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
exec python3 "$ROOT/scripts/lib/install.py" "$@"
