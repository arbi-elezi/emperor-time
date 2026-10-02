<#
.SYNOPSIS
  Thin twin of good-tests.sh — writing-good-tests HARD-GATE card via Python core.
#>
[CmdletBinding()]
param(
    [Parameter(ValueFromRemainingArguments = $true)]
    [string[]]$Rest
)
$ErrorActionPreference = 'Stop'
$root = (Resolve-Path (Join-Path $PSScriptRoot '..')).Path
$py = Join-Path $root 'scripts/lib/good_tests.py'
. (Join-Path $PSScriptRoot 'lib/resolve-emperor-python.ps1')
Invoke-EmperorPython $py @Rest
exit $LASTEXITCODE
