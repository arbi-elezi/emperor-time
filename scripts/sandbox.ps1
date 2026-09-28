<#
.SYNOPSIS
  Alias → context.ps1 (sandbox)
#>
[CmdletBinding()]
param([Parameter(ValueFromRemainingArguments=$true)][string[]]$ArgsRemain)
$ErrorActionPreference = 'Stop'
$ctx = Join-Path $PSScriptRoot 'context.ps1'
& $ctx sandbox @ArgsRemain; exit $LASTEXITCODE
