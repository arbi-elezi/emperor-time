<#
.SYNOPSIS
  Thin twin of harness-plan.sh — harness tool+force planner via Python core.
#>
[CmdletBinding()]
param(
    [Parameter(ValueFromRemainingArguments = $true)]
    [string[]]$Rest
)
$ErrorActionPreference = 'Stop'
$root = (Resolve-Path (Join-Path $PSScriptRoot '..')).Path
$py = Join-Path $root 'scripts/lib/harness_plan.py'
& python3 $py @Rest
exit $LASTEXITCODE
