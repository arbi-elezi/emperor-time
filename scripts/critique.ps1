<#
.SYNOPSIS
  Thin twin of critique.sh — Judgment self-critique eight-count via Python core.
#>
[CmdletBinding()]
param(
    [Parameter(ValueFromRemainingArguments = $true)]
    [string[]]$Rest
)
$ErrorActionPreference = 'Stop'
$root = (Resolve-Path (Join-Path $PSScriptRoot '..')).Path
$py = Join-Path $root 'scripts/lib/critique.py'
& python3 $py @Rest
exit $LASTEXITCODE
