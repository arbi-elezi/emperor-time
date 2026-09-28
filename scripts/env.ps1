<#
.SYNOPSIS
  Alias → context.ps1 (env)
#>
[CmdletBinding()]
param([Parameter(ValueFromRemainingArguments=$true)][string[]]$ArgsRemain)
$ErrorActionPreference = 'Stop'
$ctx = Join-Path $PSScriptRoot 'context.ps1'
& $ctx env @ArgsRemain; exit $LASTEXITCODE
