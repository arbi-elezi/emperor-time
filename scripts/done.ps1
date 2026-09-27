<#
.SYNOPSIS
  Thin twin of done.sh — agent-defined DONE probes via Python core.
.EXAMPLE
  .\done.ps1 .emperor/tasks/demo
#>
[CmdletBinding()]
param(
    [Parameter(ValueFromRemainingArguments = $true)]
    [string[]]$Rest
)
$ErrorActionPreference = 'Stop'
$root = (Resolve-Path (Join-Path $PSScriptRoot '..')).Path
$py = Join-Path $root 'scripts/lib/done.py'
& python3 $py @Rest
exit $LASTEXITCODE
