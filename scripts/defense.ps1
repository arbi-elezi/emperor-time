<#
.SYNOPSIS
  Thin twin of defense.sh — defense-in-depth HARD-GATE card via Python core.
#>
[CmdletBinding()]
param(
    [Parameter(ValueFromRemainingArguments = $true)]
    [string[]]$Rest
)
$ErrorActionPreference = 'Stop'
$root = (Resolve-Path (Join-Path $PSScriptRoot '..')).Path
$py = Join-Path $root 'scripts/lib/defense.py'
& python3 $py @Rest
exit $LASTEXITCODE
