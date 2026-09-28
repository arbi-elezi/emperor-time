<#
.SYNOPSIS
  Alias twin: reproduce-and-bisect → reproduce Python core.
#>
[CmdletBinding()]
param(
    [Parameter(ValueFromRemainingArguments = $true)]
    [string[]]$Rest
)
$ErrorActionPreference = 'Stop'
$root = (Resolve-Path (Join-Path $PSScriptRoot '..')).Path
& bash (Join-Path $root 'scripts/reproduce.sh') @Rest
exit $LASTEXITCODE
