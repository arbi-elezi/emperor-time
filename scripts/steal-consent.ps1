<#
.SYNOPSIS
  Alias twin: steal-consent → consent Python core.
#>
[CmdletBinding()]
param(
    [Parameter(ValueFromRemainingArguments = $true)]
    [string[]]$Rest
)
$ErrorActionPreference = 'Stop'
& (Join-Path $PSScriptRoot 'consent.ps1') @Rest
exit $LASTEXITCODE
