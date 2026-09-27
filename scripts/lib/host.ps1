# Host detect for PowerShell 5.1 and pwsh. Dot-source from emperor.ps1 / boot.ps1.
# Twin of scripts/lib/host.sh — same host.env keys from Write-EmperorHostReport.
$script:EmperorOs = 'windows'
$script:EmperorShell = 'powershell'
$script:EmperorWsl = 0
$script:EmperorInterop = 0
$script:EmperorMnt = ''
$script:EmperorWinRoot = ''

if ($PSVersionTable.PSEdition -eq 'Core') { $script:EmperorShell = 'pwsh' }

if ($env:OS -ne 'Windows_NT') {
    # Prefer automatic variables when present (pwsh); else uname-ish fallbacks.
    $isWin = $false
    try { if ($IsWindows) { $isWin = $true } } catch {}
    $isMac = $false
    try { if ($IsMacOS) { $isMac = $true } } catch {}
    if ($env:WSL_DISTRO_NAME -or $env:WSL_INTEROP) {
        $script:EmperorOs = 'wsl'
        $script:EmperorWsl = 1
        if (Get-Command cmd.exe -ErrorAction SilentlyContinue) { $script:EmperorInterop = 1 }
        if (Test-Path '/mnt/c') { $script:EmperorMnt = '/mnt'; $script:EmperorWinRoot = '/mnt/c' }
        elseif (Test-Path '/mnt/wslg') { $script:EmperorMnt = '/mnt' }
    } elseif ($isMac) {
        $script:EmperorOs = 'macos'
    } elseif (-not $isWin) {
        $script:EmperorOs = 'linux'
    }
}

try {
    [Console]::OutputEncoding = [System.Text.UTF8Encoding]::new($false)
    $OutputEncoding = [Console]::OutputEncoding
} catch {}
if (-not $env:EMPEROR_ENCODING) { $env:EMPEROR_ENCODING = 'UTF-8' }
$env:EMPEROR_OS = $script:EmperorOs
$env:EMPEROR_SHELL = $script:EmperorShell
$env:EMPEROR_WSL = [string]$script:EmperorWsl
$env:EMPEROR_WIN_INTEROP = [string]$script:EmperorInterop

function Convert-EmperorToWin([string]$Path) {
    $wslpath = Get-Command wslpath -ErrorAction SilentlyContinue
    if ($wslpath) { & wslpath -w $Path; return }
    return $Path
}
function Convert-EmperorToPosix([string]$Path) {
    $wsl = Get-Command wsl.exe -ErrorAction SilentlyContinue
    if ($wsl) { & wsl.exe -e wslpath -u $Path; return }
    return $Path
}
function Invoke-EmperorWsl([string[]]$Cmd) {
    $wsl = Get-Command wsl.exe -ErrorAction SilentlyContinue
    if (-not $wsl) { throw 'wsl.exe not on PATH' }
    & wsl.exe -e @Cmd
    return $LASTEXITCODE
}
function Write-EmperorHostReport {
    # Canonical report line lives in host.py (closes bash↔ps1 drift).
    $hostPy = Join-Path $PSScriptRoot 'host.py'
    if (-not (Test-Path $hostPy)) {
        $hostPy = Join-Path (Join-Path $PSScriptRoot 'lib') 'host.py'
    }
    if ((Test-Path $hostPy) -and (Get-Command python3 -ErrorAction SilentlyContinue)) {
        & python3 $hostPy --report
        return
    }
    $enc = if ($env:EMPEROR_ENCODING) { $env:EMPEROR_ENCODING } else { 'UTF-8' }
    'os={0} shell={1} wsl={2} win_interop={3} encoding={4} mnt={5} win_root={6}' -f `
        $script:EmperorOs, $script:EmperorShell, $script:EmperorWsl, `
        $script:EmperorInterop, $enc, $script:EmperorMnt, $script:EmperorWinRoot
}
