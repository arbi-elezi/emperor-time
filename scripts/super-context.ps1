<#
.SYNOPSIS
  Alias → context.ps1 (super-context)
#>
[CmdletBinding()]
param([Parameter(ValueFromRemainingArguments=$true)][string[]]$ArgsRemain)
$ErrorActionPreference = 'Stop'
$ctx = Join-Path $PSScriptRoot 'context.ps1'
& $ctx @ArgsRemain; exit $LASTEXITCODE
