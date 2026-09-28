<#
.SYNOPSIS
  Alias twin: holy-triage → triage Python core.
#>
[CmdletBinding()]
param(
    [Parameter(ValueFromRemainingArguments = $true)]
    [string[]]$Rest
)
$ErrorActionPreference = 'Stop'
& (Join-Path $PSScriptRoot 'triage.ps1') @Rest
exit $LASTEXITCODE
