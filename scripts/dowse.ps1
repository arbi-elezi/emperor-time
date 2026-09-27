<#
.SYNOPSIS
  Thin twin of dowse.sh — Dowsing Chain Mode 2 via Python core.
.EXAMPLE
  .\dowse.ps1
  .\dowse.ps1 -CheckAuth
  .\dowse.ps1 -AsJson
  .\dowse.ps1 -SkipVersions
#>
[CmdletBinding()]
param(
    [switch]$CheckAuth,
    [switch]$AsJson,
    [switch]$SkipVersions
)
$ErrorActionPreference = 'Stop'
$root = (Resolve-Path (Join-Path $PSScriptRoot '..')).Path
$py = Join-Path $root 'scripts/lib/dowse.py'
$flags = @()
if ($CheckAuth) { $flags += '--check-auth' }
if ($AsJson) { $flags += '--as-json' }
if ($SkipVersions) { $flags += '--skip-versions' }
& python3 $py @flags
exit $LASTEXITCODE
