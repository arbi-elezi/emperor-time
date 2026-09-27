<#
.SYNOPSIS
  Thin twin of heal.sh — four-phase debug checklist via Python core.
#>
[CmdletBinding()]
param(
    [Parameter(ValueFromRemainingArguments = $true)]
    [string[]]$Rest
)
$ErrorActionPreference = 'Stop'
$root = (Resolve-Path (Join-Path $PSScriptRoot '..')).Path
$py = Join-Path $root 'scripts/lib/debug_phases.py'
& python3 $py @Rest
exit $LASTEXITCODE
