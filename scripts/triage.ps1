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
. (Join-Path $PSScriptRoot 'lib/resolve-emperor-python.ps1')
Invoke-EmperorPython $py @Rest
exit $LASTEXITCODE
