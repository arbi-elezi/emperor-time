<#
.SYNOPSIS
  Dowsing Chain, Mode 2 - scan this machine for enlistable coding agents.
.DESCRIPTION
  READ-ONLY by design (Vow of Consent): detects binaries on PATH and probes
  --version. It never installs anything, never runs logins, never reads
  credential or config files. Auth probes run ONLY with -CheckAuth and only
  use the whitelisted harmless status commands from references/agent-registry.md.
.EXAMPLE
  .\dowse.ps1                 # detection + versions
  .\dowse.ps1 -CheckAuth      # also run safe auth status probes
  .\dowse.ps1 -AsJson         # machine-readable roster for an orchestrator
.NOTES
  Runs under Windows PowerShell 5.1+ and pwsh on macOS/Linux (dowse.sh is the
  native alternative there).
#>
[CmdletBinding()]
param(
    [switch]$CheckAuth,
    [switch]$AsJson,
    [switch]$SkipVersions
)

$agents = @(
    @{ Name = 'Claude Code';  Bin = 'claude';   Core = $true;  AuthCmd = $null;                    Headless = 'claude -p "<prompt>" --output-format json'; Login = 'run `claude` interactively (first-run login)' }
    @{ Name = 'Kimi CLI';     Bin = 'kimi';     Core = $true;  AuthCmd = $null;                    Headless = 'no documented print flag - check `kimi --help`; kimi-agent-sdk; `kimi acp`'; Login = 'run `kimi`, then /login' }
    @{ Name = 'Codex CLI';    Bin = 'codex';    Core = $true;  AuthCmd = @('login','status');      Headless = 'codex exec "<prompt>"'; Login = 'codex login  (headless: codex login --device-auth)' }
    @{ Name = 'Copilot CLI';  Bin = 'copilot';  Core = $true;  AuthCmd = $null;                    Headless = 'copilot -p "<prompt>" -s --no-ask-user'; Login = 'see `copilot --help` login flow' }
    @{ Name = 'opencode';     Bin = 'opencode'; Core = $true;  AuthCmd = $null;                    Headless = 'opencode run "<prompt>"'; Login = 'see `opencode --help` / auth subcommand' }
    @{ Name = 'Ollama';       Bin = 'ollama';   Core = $true;  AuthCmd = @('list');                Headless = 'ollama run <model> "<prompt>"'; Login = 'none (local); daemon must be running' }
    @{ Name = 'GitHub CLI';   Bin = 'gh';       Core = $false; AuthCmd = @('auth','status');       Headless = '(adjacent tooling, not an agent)'; Login = 'gh auth login' }
    @{ Name = 'Aider';        Bin = 'aider';    Core = $false; AuthCmd = $null;                    Headless = 'verify at dowse: aider --help'; Login = 'API key env vars (client sets)' }
    @{ Name = 'Gemini CLI';   Bin = 'gemini';   Core = $false; AuthCmd = $null;                    Headless = 'verify at dowse: gemini --help'; Login = 'see `gemini --help`' }
    @{ Name = 'Goose';        Bin = 'goose';    Core = $false; AuthCmd = $null;                    Headless = 'verify at dowse: goose --help'; Login = 'see `goose --help`' }
    @{ Name = 'Qwen Code';    Bin = 'qwen';     Core = $false; AuthCmd = $null;                    Headless = 'verify at dowse: qwen --help'; Login = 'see `qwen --help`' }
)

$roster = @()
foreach ($a in $agents) {
    $cmd = Get-Command $a.Bin -ErrorAction SilentlyContinue
    $entry = [ordered]@{
        Agent    = $a.Name
        Binary   = $a.Bin
        Status   = 'NOT INSTALLED'
        Version  = ''
        Auth     = 'unchecked'
        Headless = $a.Headless
        SignIn   = $a.Login
    }
    if ($null -ne $cmd) {
        $entry.Status = 'DETECTED'
        if (-not $SkipVersions) {
            try {
                $v = & $a.Bin --version 2>$null | Select-Object -First 1
                if ($null -ne $v) { $entry.Version = [string]$v }
            } catch { $entry.Version = '(version probe failed)' }
        }
        if ($CheckAuth) {
            if ($null -ne $a.AuthCmd) {
                # Bounded wait so a blocking probe (e.g. `ollama list` with the
                # daemon down) cannot hang the whole scan.
                $outFile = [IO.Path]::GetTempFileName()
                $errFile = [IO.Path]::GetTempFileName()
                try {
                    $p = Start-Process -FilePath $a.Bin -ArgumentList $a.AuthCmd -NoNewWindow -PassThru -RedirectStandardOutput $outFile -RedirectStandardError $errFile
                    $null = $p.Handle   # PS 5.1 quirk: ExitCode stays null unless the handle is touched before exit
                    if ($p.WaitForExit(8000)) {
                        $first = ''
                        try { $first = [string](Get-Content $outFile -TotalCount 1 -ErrorAction Stop) } catch {}
                        if (-not $first) { try { $first = [string](Get-Content $errFile -TotalCount 1 -ErrorAction Stop) } catch {} }
                        if ($p.ExitCode -eq 0) { $entry.Auth = 'OK: ' + $first }
                        else { $entry.Auth = 'NEEDS SIGN-IN (status cmd exit ' + $p.ExitCode + ')' }
                    } else {
                        try { $p.Kill() } catch {}
                        $entry.Auth = 'TIMEOUT after 8s (daemon down or cmd hung)'
                    }
                } catch { $entry.Auth = 'NEEDS SIGN-IN (status probe failed)' }
                finally { Remove-Item $outFile, $errFile -Force -ErrorAction SilentlyContinue }
            } else {
                $entry.Auth = 'no safe status cmd known - verify via `' + $a.Bin + ' --help`'
            }
        }
    }
    $roster += [pscustomobject]$entry
}

if ($AsJson) {
    $roster | ConvertTo-Json -Depth 4
    return
}

Write-Host ''
Write-Host '=== EMPEROR TIME :: DOWSING CHAIN :: machine scan ===' -ForegroundColor Magenta
Write-Host '(read-only: no installs, no logins, no credential access)'
Write-Host ''
$roster | Format-Table Agent, Status, Version, Auth -AutoSize

$detected = @($roster | Where-Object { $_.Status -eq 'DETECTED' })
Write-Host ('Detected: ' + $detected.Count + ' agent(s).')
Write-Host ''
Write-Host 'Next steps (Steal Chain protocol):'
Write-Host '  1. Verify each invocation syntax against reality:  <binary> --help'
Write-Host '  2. Agents needing sign-in: the CLIENT logs in, in a NEW terminal they open'
Write-Host '     themselves (never the orchestrator''s shell). Commands: see SignIn hints'
Write-Host '     via -AsJson or references/agent-registry.md.'
Write-Host '  3. Re-run with -CheckAuth to confirm via harmless status commands only.'
Write-Host '  4. Hand the roster to chains/steal-chain/SKILL.md for consent + dispatch.'
