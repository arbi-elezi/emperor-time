<#
.SYNOPSIS
  Thin twin of quarantine.sh — Steal quarantine via Python core.
#>
[CmdletBinding()]
param(
    [Parameter(ValueFromRemainingArguments = $true)]
    [string[]]$Rest
)
$ErrorActionPreference = 'Stop'
$root = (Resolve-Path (Join-Path $PSScriptRoot '..')).Path
$py = Join-Path $root 'scripts/lib/quarantine.py'
& python3 $py @Rest
exit $LASTEXITCODE
