<#
.SYNOPSIS
  Thin twin of context.sh — thoughttrail + super-context via Python core.
#>
[CmdletBinding()]
param(
    [Parameter(ValueFromRemainingArguments = $true)]
    [string[]]$Rest
)
$ErrorActionPreference = 'Stop'
$root = (Resolve-Path (Join-Path $PSScriptRoot '..')).Path
$py = Join-Path $root 'scripts/lib/context.py'
& python3 $py @Rest
exit $LASTEXITCODE
