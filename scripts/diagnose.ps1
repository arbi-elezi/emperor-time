<#
.SYNOPSIS
  Thin twin of diagnose.sh — diagnosing HARD-GATE card via Python core.
#>
[CmdletBinding()]
param(
    [Parameter(ValueFromRemainingArguments = $true)]
    [string[]]$Rest
)
$ErrorActionPreference = 'Stop'
$root = (Resolve-Path (Join-Path $PSScriptRoot '..')).Path
$py = Join-Path $root 'scripts/lib/diagnose.py'
& python3 $py @Rest
exit $LASTEXITCODE
