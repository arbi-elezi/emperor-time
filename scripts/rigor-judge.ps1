<#
.SYNOPSIS
  Thin twin of rigor-judge.sh — cheap effort_class recommendation via Python core.
#>
[CmdletBinding()]
param(
    [Parameter(ValueFromRemainingArguments = $true)]
    [string[]]$Rest
)
$ErrorActionPreference = 'Stop'
$root = (Resolve-Path (Join-Path $PSScriptRoot '..')).Path
$py = Join-Path $root 'scripts/lib/rigor_judge.py'
& python3 $py @Rest
exit $LASTEXITCODE
