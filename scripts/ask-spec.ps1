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
& python3 $py @Rest
exit $LASTEXITCODE
