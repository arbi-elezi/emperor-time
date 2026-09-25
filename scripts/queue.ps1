[CmdletBinding()]
param(
    [Parameter(Position = 0)][ValidateSet('list','next','add','done')]$Cmd = 'next',
    [Parameter(ValueFromRemainingArguments = $true)][string[]]$Rest
)
$ErrorActionPreference = 'Stop'
$Root = (Resolve-Path (Join-Path $PSScriptRoot '..')).Path
$Queue = if ($env:EMPEROR_QUEUE_FILE) { $env:EMPEROR_QUEUE_FILE } else { Join-Path $Root '.emperor/queue.md' }
$dir = Split-Path $Queue
if (-not (Test-Path $dir)) { New-Item -ItemType Directory -Force -Path $dir | Out-Null }
if (-not (Test-Path $Queue)) { "# Emperor queue`n`n- [ ] (empty — add a line or connect gh/Linear)`n" | Set-Content $Queue }
function LocalOpen { Select-String -Path $Queue -Pattern '^- \[ \]' | ForEach-Object { $_.Line } }
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
        if (Get-Command gh -ErrorAction SilentlyContinue) {
            $item = gh issue list --state open --limit 1 --json number,title 2>$null
            if ($item -and $item -ne '[]') { Write-Host "NEXT gh: $item"; exit 0 }
        }
        if ($env:LINEAR_API_KEY) { Write-Host 'NEXT linear: key present — query with consent'; exit 0 }
        $line = @(LocalOpen | Select-Object -First 1)
        if ($line -and $line -notmatch '\(empty') { Write-Host "NEXT local: $line"; exit 0 }
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
            if (-not $hit -and $_ -match '^- \[ \]' -and $_.Contains($pat)) {
                $hit = $true
                $_ -replace '^- \[ \]', '- [x]'
            } else { $_ }
        }
        $c | Set-Content $Queue
        Write-Host "CHECKED: $pat"
    }
}
