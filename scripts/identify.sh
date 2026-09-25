#!/usr/bin/env bash
# Language-agnostic artifact survey. No preferred stack.
set -euo pipefail
ROOT="${1:-.}"
echo "== identify $ROOT =="
if command -v find >/dev/null 2>&1; then
  echo "-- extensions --"
  find "$ROOT" -type f ! -path '*/.git/*' ! -path '*/.emperor/*' ! -path '*/node_modules/*' \
    | sed 's/.*\.//' | grep -E '^[A-Za-z0-9]+$' | sort | uniq -c | sort -nr | head -n 40
fi
echo "-- named fossils --"
for pat in '*.pas' '*.pp' '*.dpr' '*.asm' '*.s' '*.S' '*.inc' '*.cbl' '*.cob' '*.for' '*.f' '*.f90' '*.vhd' '*.vhdl' '*.rel' '*.hex' '*.bin' '*.rom' 'Makefile' 'makefile' '*.mak' '*.lpr'; do
  n=$(find "$ROOT" -type f -name "$pat" ! -path '*/.git/*' 2>/dev/null | wc -l | tr -d ' ')
  [[ "$n" != 0 ]] && echo "$n $pat"
done
echo "-- shebangs --"
find "$ROOT" -type f ! -path '*/.git/*' -size -200k 2>/dev/null | head -n 200 | while read -r f; do
  head -n1 "$f" 2>/dev/null | grep -q '^#!' && echo "$f: $(head -n1 "$f")"
done | head -n 30
exit 0
