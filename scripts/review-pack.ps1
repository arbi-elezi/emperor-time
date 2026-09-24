<#
.SYNOPSIS
  Isolated review pack: SHAs + diff + criteria. No author CoT.
#>
[CmdletBinding()]
param(
    [Parameter(Mandatory=$true,Position=0)][string]$TaskDir,
    [string]$Base = 'HEAD~1',
    [string]$Head = 'HEAD'
)
$ErrorActionPreference = 'Stop'
if (-not (Test-Path $TaskDir -PathType Container)) { Write-Error "missing $TaskDir"; exit 1 }
$out = Join-Path $TaskDir 'review-pack'
New-Item -ItemType Directory -Force -Path $out | Out-Null
$meta = @('# Isolated review pack', "- task: $TaskDir", "- generated: $((Get-Date).ToUniversalTime().ToString('yyyy-MM-ddTHH:mm:ssZ'))")
$inGit = [bool](Get-Command git -ErrorAction SilentlyContinue) -and (git rev-parse --is-inside-work-tree 2>$null)
if ($inGit) {
    $meta += "- base: $(git rev-parse $Base)"
    $meta += "- head: $(git rev-parse $Head)"
} else { $meta += '- base/head: not a git repo' }
Set-Content (Join-Path $out 'meta.md') -Value $meta
$order = Join-Path $TaskDir 'work-order.md'
if (Test-Path $order) { Copy-Item $order (Join-Path $out 'criteria.md') -Force }
if ($inGit) {
    git diff "$Base..$Head" | Out-File (Join-Path $out 'diff.patch')
    git diff --stat "$Base..$Head" | Out-File (Join-Path $out 'diffstat.txt')
}
$claims = Join-Path $TaskDir 'claims.md'
if (Test-Path $claims) { Copy-Item $claims (Join-Path $out 'claims.md') -Force }
Write-Host "REVIEW PACK: $out"
Get-ChildItem $out | Format-Table Name, Length
