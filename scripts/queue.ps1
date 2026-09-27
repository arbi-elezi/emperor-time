[CmdletBinding()]
param(
    [Parameter(Position = 0)][ValidateSet('list','next','add','done')]$Cmd = 'next',
    [Parameter(ValueFromRemainingArguments = $true)][string[]]$Rest
)
# Kanban statuses (WIP=1): [ ] ready · [~] active · [x] done · [!] blocked
$ErrorActionPreference = 'Stop'
$Root = (Resolve-Path (Join-Path $PSScriptRoot '..')).Path
$Queue = if ($env:EMPEROR_QUEUE_FILE) { $env:EMPEROR_QUEUE_FILE } else { Join-Path $Root '.emperor/queue.md' }
$dir = Split-Path $Queue
if (-not (Test-Path $dir)) { New-Item -ItemType Directory -Force -Path $dir | Out-Null }
if (-not (Test-Path $Queue)) {
    @"
# Emperor queue
# WIP=1 — one [~] active at a time. Statuses: [ ] ready · [~] active · [x] done · [!] blocked
#
# Empty — add: - [ ] <task>  (or connect gh/Linear). Placeholder/parentheses-empty lines are ignored.

Local backlog when GitHub issues / Linear are not connected.
"@ | Set-Content $Queue
}
function IsPlaceholder([string]$line) {
    if ($line -match '\(empty') { return $true }
    if ($line -match '^- \[[ ~!]\] *$') { return $true }
    if ($line -match '^- \[[ ~!]\] +\(.*\) *$') { return $true }
    return $false
}
function LocalOpen {
    Select-String -Path $Queue -Pattern '^- \[([ ~!])\]' | ForEach-Object { $_.Line } | Where-Object { -not (IsPlaceholder $_) }
}
function LocalReady {
    Select-String -Path $Queue -Pattern '^- \[ \]' | ForEach-Object { $_.Line } | Where-Object { -not (IsPlaceholder $_) }
}
function LocalActive {
    Select-String -Path $Queue -Pattern '^- \[~\]' | ForEach-Object { $_.Line } | Where-Object { -not (IsPlaceholder $_) }
}
function PromoteFirstReady {
    $c = Get-Content $Queue
    $promoted = $null
    $c = $c | ForEach-Object {
        if ($null -eq $promoted -and $_ -match '^- \[ \]' -and -not (IsPlaceholder $_)) {
            $promoted = ($_ -replace '^- \[ \]', '- [~]')
            $promoted
        } else { $_ }
    }
    $c | Set-Content $Queue
    return $promoted
}
switch ($Cmd) {
    'list' {
        Write-Host "== local $Queue =="
        LocalOpen
        if (Get-Command gh -ErrorAction SilentlyContinue) {
            Write-Host '== gh issues =='
            gh issue list --state open --limit 10
        }
    }
    'next' {
        $src = if ($env:EMPEROR_QUEUE_SOURCE) { $env:EMPEROR_QUEUE_SOURCE } else { 'auto' }
        if (($src -eq 'gh' -or $src -eq 'auto') -and (Get-Command gh -ErrorAction SilentlyContinue)) {
            $item = gh issue list --state open --limit 1 --json number,title --jq '.[] | "#\(.number) \(.title)"' 2>$null
            if ($item) { Write-Host "NEXT gh: $item"; exit 0 }
        }
        if ($src -eq 'linear' -or ($src -eq 'auto' -and $env:LINEAR_API_KEY)) {
            Write-Host 'NEXT linear: key present — agent must query Linear with client consent; script will not ship tokens.'
            exit 0
        }
        $active = @(LocalActive | Select-Object -First 1)
        if ($active) {
            Write-Host "NEXT local (active): $active"
            Write-Host 'WIP=1: refuse second active — finish current or: queue done <substring>'
            exit 0
        }
        $line = @(LocalReady | Select-Object -First 1)
        if ($line) {
            $promoted = PromoteFirstReady
            if ($promoted) { Write-Host "NEXT local: $promoted"; exit 0 }
        }
        Write-Host "NEXT none: queue empty. Add a line to $Queue or pass a task."
        exit 2
    }
    'add' {
        if (-not $Rest) { Write-Error 'usage: queue.ps1 add <text>'; exit 2 }
        Add-Content $Queue ("- [ ] " + ($Rest -join ' '))
        Write-Host ("QUEUED: " + ($Rest -join ' '))
    }
    'done' {
        if (-not $Rest) { Write-Error 'usage: queue.ps1 done <substring>'; exit 2 }
        $pat = $Rest[0]
        $c = Get-Content $Queue
        $hit = $false
        $c = $c | ForEach-Object {
            if (-not $hit -and $_ -match '^- \[[ ~!]\]' -and $_.Contains($pat)) {
                $hit = $true
                $_ -replace '^- \[[ ~!]\]', '- [x]'
            } else { $_ }
        }
        $c | Set-Content $Queue
        Write-Host "CHECKED: $pat"
    }
}
