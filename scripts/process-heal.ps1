<#
.SYNOPSIS
  Thin twin of process-heal.sh — holy process-healing via Python core.
#>
[CmdletBinding()]
param(
    [Parameter(ValueFromRemainingArguments = $true)]
    [string[]]$Rest
)
$ErrorActionPreference = 'Stop'
$root = (Resolve-Path (Join-Path $PSScriptRoot '..')).Path
$py = Join-Path $root 'scripts/lib/process_heal.py'
& python3 $py @Rest
exit $LASTEXITCODE
