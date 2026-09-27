<#
.SYNOPSIS
  Thin twin of tdd.sh — TDD iron-law / RGR checklist via Python core.
#>
[CmdletBinding()]
param(
    [Parameter(ValueFromRemainingArguments = $true)]
    [string[]]$Rest
)
$ErrorActionPreference = 'Stop'
$root = (Resolve-Path (Join-Path $PSScriptRoot '..')).Path
$py = Join-Path $root 'scripts/lib/tdd.py'
& python3 $py @Rest
exit $LASTEXITCODE
