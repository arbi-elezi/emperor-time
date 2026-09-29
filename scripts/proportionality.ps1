<#
.SYNOPSIS
  Thin twin of proportionality.sh — anti-loop via Python core.
#>
[CmdletBinding()]
param(
    [Parameter(ValueFromRemainingArguments = $true)]
    [string[]]$Rest
)
$ErrorActionPreference = 'Stop'
$root = (Resolve-Path (Join-Path $PSScriptRoot '..')).Path
$py = Join-Path $root 'scripts/lib/proportionality.py'
& python3 $py @Rest
exit $LASTEXITCODE
