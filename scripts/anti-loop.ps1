<#
.SYNOPSIS
  Alias twin: anti-loop → proportionality Python core.
#>
[CmdletBinding()]
param(
    [Parameter(ValueFromRemainingArguments = $true)]
    [string[]]$Rest
)
$ErrorActionPreference = 'Stop'
$here = $PSScriptRoot
& (Join-Path $here 'proportionality.ps1') @Rest
exit $LASTEXITCODE
