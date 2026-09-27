<#
.SYNOPSIS
  Thin twin of review-pack.sh — isolated review pack via Python core.
.EXAMPLE
  .\review-pack.ps1 .emperor/tasks/demo HEAD~1 HEAD
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
