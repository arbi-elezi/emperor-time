<#
.SYNOPSIS
  Thin twin of finish.sh — git finish ENV/MENU + suite-green HARD-GATE via Python core.
  Does not merge, push, or delete.
  --reject-red-suite / --require-green refuse menu without green suite.
#>
[CmdletBinding()]
param(
    [Parameter(ValueFromRemainingArguments = $true)]
    [string[]]$Rest
)
$ErrorActionPreference = 'Stop'
$root = (Resolve-Path (Join-Path $PSScriptRoot '..')).Path
$py = Join-Path $root 'scripts/lib/finish.py'
& python3 $py @Rest
exit $LASTEXITCODE
