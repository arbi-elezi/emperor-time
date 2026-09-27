<#
.SYNOPSIS
  Thin twin of parallel.sh — parallel-dispatch checklist via Python core.
#>
[CmdletBinding()]
param(
    [Parameter(ValueFromRemainingArguments = $true)]
    [string[]]$Rest
)
$ErrorActionPreference = 'Stop'
$root = (Resolve-Path (Join-Path $PSScriptRoot '..')).Path
$py = Join-Path $root 'scripts/lib/parallel.py'
& python3 $py @Rest
exit $LASTEXITCODE
