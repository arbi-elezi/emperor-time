<#
.SYNOPSIS
  Alias twin: self-critique → critique.py eight-count HARD-GATE.
#>
[CmdletBinding()]
param(
    [Parameter(ValueFromRemainingArguments = $true)]
    [string[]]$Rest
)
$ErrorActionPreference = 'Stop'
$root = (Resolve-Path (Join-Path $PSScriptRoot '..')).Path
& (Join-Path $root 'scripts/critique.ps1') @Rest
exit $LASTEXITCODE
