<#
.SYNOPSIS
  Thin twin of route.sh — trigger→skill router MVP via Python core.
.EXAMPLE
  .\route.ps1 "lost pascal tree"
  .\route.ps1 "hello.f90"
#>
[CmdletBinding()]
param(
    [Parameter(ValueFromRemainingArguments = $true)]
    [string[]]$Rest
)
$ErrorActionPreference = 'Stop'
$root = (Resolve-Path (Join-Path $PSScriptRoot '..')).Path
$py = Join-Path $root 'scripts/lib/route.py'
& python3 $py @Rest
exit $LASTEXITCODE
