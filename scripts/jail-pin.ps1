<#
.SYNOPSIS
  Alias twin: jail-pin → pin-and-consent Python core.
#>
[CmdletBinding()]
param(
    [Parameter(ValueFromRemainingArguments = $true)]
    [string[]]$Rest
)
$ErrorActionPreference = 'Stop'
$here = $PSScriptRoot
& (Join-Path $here 'pin-and-consent.ps1') @Rest
exit $LASTEXITCODE
