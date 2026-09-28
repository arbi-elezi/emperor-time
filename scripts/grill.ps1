<#
.SYNOPSIS
  Thin twin of grill.sh — grill/brainstorm checklist + path-taxonomy HARD-GATE via Python core.
  --reject-no-path / --reject-stage-skip / --reject-impl-before-approval / --check-path
  refuse missing path, skipped stage, or impl before stage approval.
#>
[CmdletBinding()]
param(
    [Parameter(ValueFromRemainingArguments = $true)]
    [string[]]$Rest
)
$ErrorActionPreference = 'Stop'
$root = (Resolve-Path (Join-Path $PSScriptRoot '..')).Path
$py = Join-Path $root 'scripts/lib/grill.py'
& python3 $py @Rest
exit $LASTEXITCODE
