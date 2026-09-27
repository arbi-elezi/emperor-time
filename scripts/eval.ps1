<#
.SYNOPSIS
  Thin twin of eval.sh — structural evals via Python core.
  Does not spawn a model. Exit 0 = EVALS PASSED, 1 = EVALS FAILED.
#>
[CmdletBinding()]
param(
    [Parameter(ValueFromRemainingArguments = $true)]
    [string[]]$Rest
)
$ErrorActionPreference = 'Stop'
$root = (Resolve-Path (Join-Path $PSScriptRoot '..')).Path
$py = Join-Path $root 'scripts/lib/eval.py'
& python3 $py @Rest
exit $LASTEXITCODE
