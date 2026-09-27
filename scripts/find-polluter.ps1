<#
.SYNOPSIS
  Thin twin of find-polluter.sh — find-polluter HARD-GATE card via Python core.
#>
[CmdletBinding()]
param(
    [Parameter(ValueFromRemainingArguments = $true)]
    [string[]]$Rest
)
$ErrorActionPreference = 'Stop'
$root = (Resolve-Path (Join-Path $PSScriptRoot '..')).Path
$py = Join-Path $root 'scripts/lib/polluter.py'
& python3 $py @Rest
exit $LASTEXITCODE
