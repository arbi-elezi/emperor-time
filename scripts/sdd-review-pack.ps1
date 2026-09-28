<#
.SYNOPSIS
  Thin twin of sdd-review-pack.sh — sdd-review-pack via Python core.
#>
[CmdletBinding()]
param(
    [Parameter(ValueFromRemainingArguments = $true)]
    [string[]]$Rest
)
$ErrorActionPreference = 'Stop'
$root = (Resolve-Path (Join-Path $PSScriptRoot '..')).Path
$py = Join-Path $root 'scripts/lib/sdd_review_pack.py'
& python3 $py @Rest
exit $LASTEXITCODE
