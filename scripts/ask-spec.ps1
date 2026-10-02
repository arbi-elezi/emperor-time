<#
.SYNOPSIS
  Thin twin of ask-spec.sh — ask→spec via Python core.
#>
[CmdletBinding()]
param(
    [Parameter(ValueFromRemainingArguments = $true)]
    [string[]]$Rest
)
$ErrorActionPreference = 'Stop'
$root = (Resolve-Path (Join-Path $PSScriptRoot '..')).Path
$py = Join-Path $root 'scripts/lib/ask_spec.py'
. (Join-Path $PSScriptRoot 'lib/resolve-emperor-python.ps1')
Invoke-EmperorPython $py @Rest
exit $LASTEXITCODE
