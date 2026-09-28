<#
.SYNOPSIS
  Thin twin of consent.sh — Steal consent-protocol via Python core.
#>
[CmdletBinding()]
param(
    [Parameter(ValueFromRemainingArguments = $true)]
    [string[]]$Rest
)
$ErrorActionPreference = 'Stop'
$root = (Resolve-Path (Join-Path $PSScriptRoot '..')).Path
$py = Join-Path $root 'scripts/lib/consent.py'
& python3 $py @Rest
exit $LASTEXITCODE
