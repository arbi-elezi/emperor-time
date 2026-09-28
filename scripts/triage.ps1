<#
.SYNOPSIS
  Thin twin of triage.sh — holy triage via Python core.
#>
[CmdletBinding()]
param(
    [Parameter(ValueFromRemainingArguments = $true)]
    [string[]]$Rest
)
$ErrorActionPreference = 'Stop'
$root = (Resolve-Path (Join-Path $PSScriptRoot '..')).Path
$py = Join-Path $root 'scripts/lib/triage.py'
& python3 $py @Rest
exit $LASTEXITCODE
