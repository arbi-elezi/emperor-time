<#
.SYNOPSIS
  Alias twin: breach → verdict.py hidden-breach HARD-GATE.
#>
[CmdletBinding()]
param(
    [Parameter(ValueFromRemainingArguments = $true)]
    [string[]]$Rest
)
$ErrorActionPreference = 'Stop'
$root = (Resolve-Path (Join-Path $PSScriptRoot '..')).Path
& (Join-Path $root 'scripts/verdict.ps1') @Rest
exit $LASTEXITCODE
