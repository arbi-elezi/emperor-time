<#
.SYNOPSIS
  Thin twin of queue.sh — local / GitHub / Linear work picker via Python core.
.EXAMPLE
  .\queue.ps1 next
  .\queue.ps1 add ship the widget
#>
[CmdletBinding()]
param(
    [Parameter(ValueFromRemainingArguments = $true)]
    [string[]]$Rest
)
$ErrorActionPreference = 'Stop'
$root = (Resolve-Path (Join-Path $PSScriptRoot '..')).Path
$py = Join-Path $root 'scripts/lib/queue.py'
& python3 $py @Rest
exit $LASTEXITCODE
