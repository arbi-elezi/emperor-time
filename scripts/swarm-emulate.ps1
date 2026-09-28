<#
.SYNOPSIS
  Alias twin: swarm-emulate → steal-flow Python core.
#>
[CmdletBinding()]
param(
    [Parameter(ValueFromRemainingArguments = $true)]
    [string[]]$Rest
)
$ErrorActionPreference = 'Stop'
& (Join-Path $PSScriptRoot 'steal-flow.ps1') @Rest
exit $LASTEXITCODE
