<#
.SYNOPSIS
  Alias twin: steal-quarantine → quarantine Python core.
#>
[CmdletBinding()]
param(
    [Parameter(ValueFromRemainingArguments = $true)]
    [string[]]$Rest
)
$ErrorActionPreference = 'Stop'
& (Join-Path $PSScriptRoot 'quarantine.ps1') @Rest
exit $LASTEXITCODE
