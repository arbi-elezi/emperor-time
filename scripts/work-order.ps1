<#
.SYNOPSIS
  Thin twin of work-order.sh — plan header + Task-N structure via Python core.
#>
[CmdletBinding()]
param(
    [Parameter(ValueFromRemainingArguments = $true)]
    [string[]]$Rest
)
$ErrorActionPreference = 'Stop'
$root = (Resolve-Path (Join-Path $PSScriptRoot '..')).Path
$py = Join-Path $root 'scripts/lib/work_order.py'
& python3 $py @Rest
exit $LASTEXITCODE
