<#
.SYNOPSIS
  Thin twin of reproduce.sh — reproduce-and-bisect via Python core.
#>
[CmdletBinding()]
param(
    [Parameter(ValueFromRemainingArguments = $true)]
    [string[]]$Rest
)
$ErrorActionPreference = 'Stop'
$root = (Resolve-Path (Join-Path $PSScriptRoot '..')).Path
$py = Join-Path $root 'scripts/lib/reproduce.py'
& python3 $py @Rest
exit $LASTEXITCODE
