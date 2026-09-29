<#
.SYNOPSIS
  Thin twin of pin-and-consent.sh — Jail pin-and-consent via Python core.
#>
[CmdletBinding()]
param(
    [Parameter(ValueFromRemainingArguments = $true)]
    [string[]]$Rest
)
$ErrorActionPreference = 'Stop'
$root = (Resolve-Path (Join-Path $PSScriptRoot '..')).Path
$py = Join-Path $root 'scripts/lib/pin_consent.py'
& python3 $py @Rest
exit $LASTEXITCODE
