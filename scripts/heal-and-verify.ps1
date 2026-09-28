<#
.SYNOPSIS
  Alias twin: heal-and-verify → heal_verify Python core.
#>
[CmdletBinding()]
param(
    [Parameter(ValueFromRemainingArguments = $true)]
    [string[]]$Rest
)
$ErrorActionPreference = 'Stop'
$root = (Resolve-Path (Join-Path $PSScriptRoot '..')).Path
& bash (Join-Path $root 'scripts/heal-verify.sh') @Rest
exit $LASTEXITCODE
