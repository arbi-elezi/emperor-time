<#
.SYNOPSIS
  Isolated git worktree for one swarm worker.
#>
[CmdletBinding()]
param(
    [Parameter(Mandatory=$true,Position=0)][string]$Id,
    [string]$Base = 'HEAD'
)
$ErrorActionPreference = 'Stop'
git rev-parse --is-inside-work-tree 2>$null | Out-Null
if ($LASTEXITCODE -ne 0) { Write-Error 'WORKTREE FAIL: not a git repo'; exit 1 }
$dir = Join-Path '.worktrees' $Id
$branch = "emperor/$Id"
New-Item -ItemType Directory -Force -Path '.worktrees' | Out-Null
if (Test-Path $dir) { Write-Host "WORKTREE EXISTS: $dir"; Write-Host $dir; exit 0 }
git worktree add -B $branch $dir $Base
Write-Host "WORKTREE: $dir"
