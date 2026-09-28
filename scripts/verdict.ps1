<#
.SYNOPSIS
  Thin twin of verdict.sh — Judgment verdict + Breach Register via Python core.
#>
[CmdletBinding()]
param(
    [Parameter(ValueFromRemainingArguments = $true)]
    [string[]]$Rest
)
$ErrorActionPreference = 'Stop'
$root = (Resolve-Path (Join-Path $PSScriptRoot '..')).Path
$py = Join-Path $root 'scripts/lib/verdict.py'
& python3 $py @Rest
exit $LASTEXITCODE
