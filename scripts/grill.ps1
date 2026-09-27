<#
.SYNOPSIS
  Thin twin of grill.sh — grill/brainstorm checklist via Python core.
#>
[CmdletBinding()]
param(
    [Parameter(ValueFromRemainingArguments = $true)]
    [string[]]$Rest
)
$ErrorActionPreference = 'Stop'
$root = (Resolve-Path (Join-Path $PSScriptRoot '..')).Path
$py = Join-Path $root 'scripts/lib/grill.py'
& python3 $py @Rest
exit $LASTEXITCODE
