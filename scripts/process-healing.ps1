<#
.SYNOPSIS
  Alias twin: process-healing → process-heal Python core.
#>
[CmdletBinding()]
param(
    [Parameter(ValueFromRemainingArguments = $true)]
    [string[]]$Rest
)
$ErrorActionPreference = 'Stop'
& (Join-Path $PSScriptRoot 'process-heal.ps1') @Rest
exit $LASTEXITCODE
