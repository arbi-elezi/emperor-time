<#
.SYNOPSIS
  Thin twin of forge.sh — consent-gated PR forge via Python core.
  HARD-GATE: --reject-no-pr-consent / --check-pr-consent
.EXAMPLE
  .\forge.ps1 .emperor/tasks/demo
#>
[CmdletBinding()]
param(
    [Parameter(ValueFromRemainingArguments = $true)]
    [string[]]$Rest
)
$ErrorActionPreference = 'Stop'
$root = (Resolve-Path (Join-Path $PSScriptRoot '..')).Path
$py = Join-Path $root 'scripts/lib/forge.py'
& python3 $py @Rest
exit $LASTEXITCODE
