<#
.SYNOPSIS
  Thin twin of activate.sh — SessionStart MUST-route card via Python core.
#>
[CmdletBinding()]
param(
    [Parameter(ValueFromRemainingArguments = $true)]
    [string[]]$Rest
)
$ErrorActionPreference = 'Stop'
$root = (Resolve-Path (Join-Path $PSScriptRoot '..')).Path
$py = Join-Path $root 'scripts/lib/activate.py'
& python3 $py @Rest
exit $LASTEXITCODE
