<#
.SYNOPSIS
  Thin twin of receive.sh — receiving-code-review checklist via Python core.
#>
[CmdletBinding()]
param(
    [Parameter(ValueFromRemainingArguments = $true)]
    [string[]]$Rest
)
$ErrorActionPreference = 'Stop'
$root = (Resolve-Path (Join-Path $PSScriptRoot '..')).Path
$py = Join-Path $root 'scripts/lib/receive.py'
& python3 $py @Rest
exit $LASTEXITCODE
