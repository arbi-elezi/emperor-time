<#
.SYNOPSIS
  Thin twin of finish.sh — git finish environment + integration menu via Python core.
  Does not merge, push, or delete.
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
