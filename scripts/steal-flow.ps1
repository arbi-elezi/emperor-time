<#
.SYNOPSIS
  Thin twin of steal-flow.sh — Steal sign-in/dispatch/swarm via Python core.
#>
[CmdletBinding()]
param(
    [Parameter(ValueFromRemainingArguments = $true)]
    [string[]]$Rest
)
$ErrorActionPreference = 'Stop'
$root = (Resolve-Path (Join-Path $PSScriptRoot '..')).Path
$py = Join-Path $root 'scripts/lib/steal_flow.py'
& python3 $py @Rest
exit $LASTEXITCODE
