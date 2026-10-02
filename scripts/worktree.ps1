<#
.SYNOPSIS
  Thin twin of worktree.sh — isolated git worktree create via Python core.
.EXAMPLE
  .\worktree.ps1 worker-1
  .\worktree.ps1 worker-1 HEAD
#>
[CmdletBinding()]
param(
    [Parameter(Mandatory = $true, Position = 0)]
    [string]$Id,

    [Parameter(Position = 1)]
    [string]$Base = 'HEAD'
)

$ErrorActionPreference = 'Stop'
$root = (Resolve-Path (Join-Path $PSScriptRoot '..')).Path
$py = Join-Path $root 'scripts/lib/worktree.py'
. (Join-Path $PSScriptRoot 'lib/resolve-emperor-python.ps1')
Invoke-EmperorPython $py $Id $Base
exit $LASTEXITCODE
