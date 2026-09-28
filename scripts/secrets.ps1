<#
.SYNOPSIS
  Alias → context.ps1 (secrets)
#>
[CmdletBinding()]
param([Parameter(ValueFromRemainingArguments=$true)][string[]]$ArgsRemain)
$ErrorActionPreference = 'Stop'
$ctx = Join-Path $PSScriptRoot 'context.ps1'
& $ctx secrets @ArgsRemain; exit $LASTEXITCODE
