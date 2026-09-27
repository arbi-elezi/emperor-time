<#
.SYNOPSIS
  Detect git finish environment and print the integration menu (twin of finish.sh).
  Does not merge, push, or delete.
#>
[CmdletBinding()]
param()
$ErrorActionPreference = 'Stop'

$null = git rev-parse --is-inside-work-tree 2>$null
if ($LASTEXITCODE -ne 0) { Write-Error 'FINISH FAIL: not a git repo'; exit 1 }

$gitDir = (Resolve-Path (git rev-parse --git-dir).Trim()).Path
$gitCommon = (Resolve-Path (git rev-parse --git-common-dir).Trim()).Path
$worktreePath = (git rev-parse --show-toplevel).Trim()
$branchRaw = git branch --show-current 2>$null
$branch = if ($branchRaw) { $branchRaw.Trim() } else { '' }
$headShort = (git rev-parse --short HEAD).Trim()
$superRaw = git rev-parse --show-superproject-working-tree 2>$null
$super = if ($superRaw) { $superRaw.Trim() } else { '' }

$kind = 'normal'
if ($super) {
    $kind = 'normal'
} elseif ($gitDir -ne $gitCommon) {
    if ($branch) { $kind = 'worktree-named' } else { $kind = 'worktree-detached' }
}

$baseGuess = 'main'
git rev-parse --verify origin/main 2>$null | Out-Null
if ($LASTEXITCODE -eq 0) {
    $baseGuess = 'main'
} else {
    git rev-parse --verify origin/master 2>$null | Out-Null
    if ($LASTEXITCODE -eq 0) { $baseGuess = 'master' }
}

Write-Host "ENV kind=$kind"
Write-Host "ENV branch=$(if ($branch) { $branch } else { 'DETACHED' })"
Write-Host "ENV head=$headShort"
Write-Host "ENV worktree=$worktreePath"
Write-Host "ENV base_guess=$baseGuess"
if ($kind -like 'worktree-*') {
    if ($worktreePath -match '[\\/]\.worktrees[\\/]' -or $worktreePath -match '[\\/]worktrees[\\/]') {
        Write-Host 'ENV cleanup_owned=yes'
    } else {
        Write-Host 'ENV cleanup_owned=no'
    }
} else {
    Write-Host 'ENV cleanup_owned=no'
}

Write-Host ''
if ($kind -eq 'worktree-detached') {
    Write-Host 'MENU detached'
    Write-Host @'
Implementation complete. You're on a detached HEAD (externally managed workspace).

1. Push as new branch and create a Pull Request
2. Keep as-is (I'll handle it later)

Which option?
'@
} else {
    Write-Host 'MENU standard'
    Write-Host @"
Implementation complete. What would you like to do?

1. Merge back to $baseGuess locally
2. Push and create a Pull Request
3. Keep the branch as-is (I'll handle it later)

Which option?
"@
}
