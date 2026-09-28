<#
.SYNOPSIS
  Alias → context.ps1 (thoughttrail)
#>
[CmdletBinding()]
param([Parameter(ValueFromRemainingArguments=$true)][string[]]$ArgsRemain)
$ErrorActionPreference = 'Stop'
$ctx = Join-Path $PSScriptRoot 'context.ps1'
if (-not $ArgsRemain) { & $ctx trail list; exit $LASTEXITCODE }
if ($ArgsRemain[0] -match '^(append|list|link)$') { & $ctx trail @ArgsRemain; exit $LASTEXITCODE }
& $ctx @ArgsRemain; exit $LASTEXITCODE
