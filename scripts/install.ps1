<#
.SYNOPSIS
  Thin twin of install.sh — deploy Emperor Time via Python core.
.EXAMPLE
  .\install.ps1 -Harness claude-code -Scope user
  .\install.ps1 -Harness claude-code -Scope project -Project C:\repos\myapp
  .\install.ps1 -Harness generic-agents -WithChainSkills
  .\install.ps1 -Harness opencode -DryRun
#>
[CmdletBinding()]
param(
    [Parameter(Mandatory = $true)]
    [ValidateSet('claude-code', 'kimi', 'codex', 'opencode', 'grok', 'generic-agents')]
    [string]$Harness,

    [ValidateSet('user', 'project')]
    [string]$Scope = 'user',

    [string]$Project = '.',

    [switch]$WithChainSkills,
    [switch]$DryRun
)

$ErrorActionPreference = 'Stop'
$root = (Resolve-Path (Join-Path $PSScriptRoot '..')).Path
$py = Join-Path $root 'scripts/lib/install.py'
$flags = @($Harness, $Scope, $Project)
if ($WithChainSkills) { $flags += '--with-chain-skills' }
if ($DryRun) { $flags += '--dry-run' }
& python3 $py @flags
exit $LASTEXITCODE
