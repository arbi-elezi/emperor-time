<#
.SYNOPSIS
  Alias → context.ps1 (sot)
#>
[CmdletBinding()]
param([Parameter(ValueFromRemainingArguments=$true)][string[]]$ArgsRemain)
$ErrorActionPreference = 'Stop'
$ctx = Join-Path $PSScriptRoot 'context.ps1'
& $ctx sot @ArgsRemain; exit $LASTEXITCODE
