<#
.SYNOPSIS
  Thin twin of pressure.sh — pressure/academic HARD-GATE card via Python core.
#>
[CmdletBinding()]
param(
    [Parameter(ValueFromRemainingArguments = $true)]
    [string[]]$Rest
)
$ErrorActionPreference = 'Stop'
$root = (Resolve-Path (Join-Path $PSScriptRoot '..')).Path
$py = Join-Path $root 'scripts/lib/pressure.py'
& python3 $py @Rest
exit $LASTEXITCODE
