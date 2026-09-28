<#
.SYNOPSIS
  Thin twin of review-pack.sh — isolated review pack + isolation HARD-GATE.
.EXAMPLE
  .\review-pack.ps1 .emperor/tasks/demo HEAD~1 HEAD
.EXAMPLE
  .\review-pack.ps1 --check-isolation .emperor/tasks/demo
.EXAMPLE
  .\review-pack.ps1 --reject-unisolated
#>
[CmdletBinding()]
param(
    [Parameter(ValueFromRemainingArguments = $true)]
    [string[]]$Rest
)
$ErrorActionPreference = 'Stop'
$root = (Resolve-Path (Join-Path $PSScriptRoot '..')).Path
$py = Join-Path $root 'scripts/lib/review_pack.py'
& python3 $py @Rest
exit $LASTEXITCODE
