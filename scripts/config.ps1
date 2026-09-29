<#
.SYNOPSIS
  Thin twin of config.sh — adjustable-rigor config via Python core.
#>
[CmdletBinding()]
param(
    [Parameter(ValueFromRemainingArguments = $true)]
    [string[]]$Rest
)
$ErrorActionPreference = 'Stop'
$root = (Resolve-Path (Join-Path $PSScriptRoot '..')).Path
$py = Join-Path $root 'scripts/lib/config.py'
& python3 $py @Rest
exit $LASTEXITCODE
