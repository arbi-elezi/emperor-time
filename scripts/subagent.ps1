<#
.SYNOPSIS
  Thin twin of subagent.sh — subagent-driven checklist via Python core.
#>
[CmdletBinding()]
param(
    [Parameter(ValueFromRemainingArguments = $true)]
    [string[]]$Rest
)
$ErrorActionPreference = 'Stop'
$root = (Resolve-Path (Join-Path $PSScriptRoot '..')).Path
$py = Join-Path $root 'scripts/lib/subagent.py'
& python3 $py @Rest
exit $LASTEXITCODE
