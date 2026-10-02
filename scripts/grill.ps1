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
. (Join-Path $PSScriptRoot 'lib/resolve-emperor-python.ps1')
Invoke-EmperorPython $py @Rest
exit $LASTEXITCODE
