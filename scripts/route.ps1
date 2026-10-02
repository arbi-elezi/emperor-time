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
. (Join-Path $PSScriptRoot 'lib/resolve-emperor-python.ps1')
Invoke-EmperorPython $py @Rest
exit $LASTEXITCODE
