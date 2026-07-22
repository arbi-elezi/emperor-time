<#
.SYNOPSIS
  Deploy Emperor Time into a harness's skill directory.
.DESCRIPTION
  Copies the skill (SKILL.md, chains/, references/, templates/, adapters/,
  scripts/) into the chosen harness's skills folder as 'emperor-time'.
  -WithChainSkills additionally exposes each chain as its own top-level skill.
  Runs under Windows PowerShell 5.1+ and pwsh on macOS/Linux (install.sh is
  the native alternative there).
.EXAMPLE
  .\install.ps1 -Harness claude-code -Scope user
  .\install.ps1 -Harness claude-code -Scope project -Project C:\repos\myapp
  .\install.ps1 -Harness kimi
  .\install.ps1 -Harness generic-agents -WithChainSkills
  .\install.ps1 -Harness opencode -DryRun
#>
[CmdletBinding()]
param(
    [Parameter(Mandatory = $true)]
    [ValidateSet('claude-code', 'kimi', 'codex', 'opencode', 'generic-agents')]
    [string]$Harness,

    [ValidateSet('user', 'project')]
    [string]$Scope = 'user',

    [string]$Project = '.',

    [switch]$WithChainSkills,
    [switch]$DryRun
)

$ErrorActionPreference = 'Stop'
$repoRoot = Split-Path -Parent $PSScriptRoot

# $HOME works in Windows PowerShell 5.1 AND pwsh on macOS/Linux; forward-slash
# child paths join correctly on every platform.
$userHome = $HOME
if (-not $userHome) { $userHome = $env:USERPROFILE }
switch ($Harness) {
    'claude-code'    { $userDir = Join-Path $userHome '.claude/skills';         $projDir = '.claude/skills' }
    'kimi'           { $userDir = Join-Path $userHome '.kimi/skills';           $projDir = '.kimi/skills' }
    'codex'          { $userDir = Join-Path $userHome '.codex/skills';          $projDir = '.codex/skills' }
    'opencode'       { $userDir = Join-Path $userHome '.opencode/skills';       $projDir = $null }
    'generic-agents' { $userDir = Join-Path $userHome '.config/agents/skills';  $projDir = '.agents/skills' }
}

if ($Scope -eq 'project') {
    if ($null -eq $projDir) { throw "Harness '$Harness' has no documented project-level skills dir - use -Scope user." }
    $resolvedProject = (Resolve-Path $Project).Path
    $destRoot = Join-Path $resolvedProject $projDir
} else {
    $destRoot = $userDir
}
$dest = Join-Path $destRoot 'emperor-time'

$items = @('SKILL.md', 'README.md', 'chains', 'references', 'templates', 'adapters', 'scripts')
$chains = @('dowsing-chain', 'chain-jail', 'judgment-chain', 'steal-chain', 'holy-chain')

Write-Host ''
Write-Host '=== EMPEROR TIME :: install ===' -ForegroundColor Magenta
Write-Host ('  source : ' + $repoRoot)
Write-Host ('  target : ' + $dest)
if ($WithChainSkills) {
    foreach ($c in $chains) { Write-Host ('  chain  : ' + (Join-Path $destRoot $c)) }
}
if ($Harness -eq 'claude-code' -and $Scope -eq 'user') {
    Write-Host '  note   : Kimi CLI reads ~/.claude/skills/ too - this install covers both.'
}
if ($DryRun) {
    Write-Host '  (dry run - nothing copied)'
    return
}

New-Item -ItemType Directory -Force -Path $dest | Out-Null
foreach ($item in $items) {
    $src = Join-Path $repoRoot $item
    if (Test-Path $src) {
        Copy-Item -Path $src -Destination $dest -Recurse -Force
    }
}

if ($WithChainSkills) {
    foreach ($c in $chains) {
        $src = Join-Path (Join-Path $repoRoot 'chains') $c
        if (Test-Path $src) {
            Copy-Item -Path $src -Destination (Join-Path $destRoot $c) -Recurse -Force
        }
    }
}

Write-Host ''
Write-Host 'Installed.' -ForegroundColor Green
switch ($Harness) {
    'claude-code'    { Write-Host 'Activate: say "emperor time" in Claude Code (or let the description auto-trigger).' }
    'kimi'           { Write-Host 'Activate: /skill:emperor-time inside a kimi session.' }
    'codex'          { Write-Host 'Activate: per Codex skill activation - verify with `codex --help`.' }
    'opencode'       { Write-Host 'Activate: opencode run --skill emperor-time  (verify flag; see adapters/opencode/).' }
    'generic-agents' { Write-Host 'Activate: any Agent-Skills-compatible harness reading ~/.config/agents/skills/.' }
}
Write-Host 'First run: execute scripts/dowse.ps1 to build the agent roster.'
