<#
.SYNOPSIS
  Thin twin of sdo.sh — skill-discovery (SDO) HARD-GATE card via Python core.
#>
[CmdletBinding()]
param(
    [Parameter(ValueFromRemainingArguments = $true)]
    [string[]]$Rest
)
$ErrorActionPreference = 'Stop'
$root = (Resolve-Path (Join-Path $PSScriptRoot '..')).Path
$py = Join-Path $root 'scripts/lib/sdo.py'
& python3 $py @Rest
exit $LASTEXITCODE
