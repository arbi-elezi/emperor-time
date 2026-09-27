<#
.SYNOPSIS
  Thin twin of execute.sh — executing-plans checklist via Python core.
#>
[CmdletBinding()]
param(
    [Parameter(ValueFromRemainingArguments = $true)]
    [string[]]$Rest
)
$ErrorActionPreference = 'Stop'
$root = (Resolve-Path (Join-Path $PSScriptRoot '..')).Path
$py = Join-Path $root 'scripts/lib/execute.py'
& python3 $py @Rest
exit $LASTEXITCODE
