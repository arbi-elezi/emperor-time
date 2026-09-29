<#
.SYNOPSIS
  Thin twin of judgment.sh — optional judgment adapter stub via Python core.
#>
[CmdletBinding()]
param(
    [Parameter(ValueFromRemainingArguments = $true)]
    [string[]]$Rest
)
$ErrorActionPreference = 'Stop'
$root = (Resolve-Path (Join-Path $PSScriptRoot '..')).Path
$py = Join-Path $root 'scripts/lib/judgment.py'
& python3 $py @Rest
exit $LASTEXITCODE
