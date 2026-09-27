<#
.SYNOPSIS
  Thin twin of skill-test.sh — testing-skills HARD-GATE card via Python core.
#>
[CmdletBinding()]
param(
    [Parameter(ValueFromRemainingArguments = $true)]
    [string[]]$Rest
)
$ErrorActionPreference = 'Stop'
$root = (Resolve-Path (Join-Path $PSScriptRoot '..')).Path
$py = Join-Path $root 'scripts/lib/skill_test.py'
& python3 $py @Rest
exit $LASTEXITCODE
