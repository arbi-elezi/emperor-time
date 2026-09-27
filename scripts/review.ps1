<#
.SYNOPSIS
  Thin twin of review.sh — request-review checklist via Python core.
#>
[CmdletBinding()]
param(
    [Parameter(ValueFromRemainingArguments = $true)]
    [string[]]$Rest
)
$ErrorActionPreference = 'Stop'
$root = (Resolve-Path (Join-Path $PSScriptRoot '..')).Path
$py = Join-Path $root 'scripts/lib/review_req.py'
& python3 $py @Rest
exit $LASTEXITCODE
