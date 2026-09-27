<#
.SYNOPSIS
  Thin twin of evidence.sh — verification-before-completion checklist via Python core.
#>
[CmdletBinding()]
param(
    [Parameter(ValueFromRemainingArguments = $true)]
    [string[]]$Rest
)
$ErrorActionPreference = 'Stop'
$root = (Resolve-Path (Join-Path $PSScriptRoot '..')).Path
$py = Join-Path $root 'scripts/lib/evidence.py'
& python3 $py @Rest
exit $LASTEXITCODE
