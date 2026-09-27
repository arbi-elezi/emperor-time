<#
.SYNOPSIS
  Thin twin of persuasion.sh — persuasion-principles HARD-GATE card via Python core.
#>
[CmdletBinding()]
param(
    [Parameter(ValueFromRemainingArguments = $true)]
    [string[]]$Rest
)
$ErrorActionPreference = 'Stop'
$root = (Resolve-Path (Join-Path $PSScriptRoot '..')).Path
$py = Join-Path $root 'scripts/lib/persuasion.py'
& python3 $py @Rest
exit $LASTEXITCODE
