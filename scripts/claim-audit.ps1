<#
.SYNOPSIS
  Thin twin of claim-audit.sh — Judgment claim-audit via Python core.
#>
[CmdletBinding()]
param(
    [Parameter(ValueFromRemainingArguments = $true)]
    [string[]]$Rest
)
$ErrorActionPreference = 'Stop'
$root = (Resolve-Path (Join-Path $PSScriptRoot '..')).Path
$py = Join-Path $root 'scripts/lib/claim_audit.py'
& python3 $py @Rest
exit $LASTEXITCODE
