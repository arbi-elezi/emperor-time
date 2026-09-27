<#
.SYNOPSIS
  Thin twin of condition-wait.sh — condition-based-waiting HARD-GATE card via Python core.
#>
[CmdletBinding()]
param(
    [Parameter(ValueFromRemainingArguments = $true)]
    [string[]]$Rest
)
$ErrorActionPreference = 'Stop'
$root = (Resolve-Path (Join-Path $PSScriptRoot '..')).Path
$py = Join-Path $root 'scripts/lib/condition_wait.py'
& python3 $py @Rest
exit $LASTEXITCODE
