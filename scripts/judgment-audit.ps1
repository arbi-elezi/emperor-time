<#
.SYNOPSIS
  Alias twin of claim-audit — Judgment claim-audit via Python core.
#>
[CmdletBinding()]
param(
    [Parameter(ValueFromRemainingArguments = $true)]
    [string[]]$Rest
)
$ErrorActionPreference = 'Stop'
& (Join-Path $PSScriptRoot 'claim-audit.ps1') @Rest
exit $LASTEXITCODE
