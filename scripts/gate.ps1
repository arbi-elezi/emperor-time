<#
.SYNOPSIS
  Thin twin of gate.sh — mechanical gates G0–G5 via Python core.
#>
[CmdletBinding()]
param(
    [Parameter(ValueFromRemainingArguments = $true)]
    [string[]]$Rest
)
$ErrorActionPreference = 'Stop'
$root = (Resolve-Path (Join-Path $PSScriptRoot '..')).Path
$py = Join-Path $root 'scripts/lib/gate.py'
& python3 $py @Rest
exit $LASTEXITCODE
