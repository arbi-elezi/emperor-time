<#
.SYNOPSIS
  Thin twin of session-discovery.sh — session locate card via Python core.
#>
[CmdletBinding()]
param(
    [Parameter(ValueFromRemainingArguments = $true)]
    [string[]]$Rest
)
$ErrorActionPreference = 'Stop'
$root = (Resolve-Path (Join-Path $PSScriptRoot '..')).Path
$py = Join-Path $root 'scripts/lib/session_discovery.py'
& python3 $py @Rest
exit $LASTEXITCODE
