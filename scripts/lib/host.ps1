# Host detect for PowerShell 5.1 and pwsh. Dot-source from emperor.ps1.
$script:EmperorOs = 'windows'
$script:EmperorWsl = $false
$script:EmperorInterop = $false
if ($env:OS -ne 'Windows_NT' -and -not $IsWindows) {
    if ($env:WSL_DISTRO_NAME -or $env:WSL_INTEROP) {
        $script:EmperorOs = 'wsl'
        $script:EmperorWsl = $true
        $script:EmperorInterop = [bool](Get-Command cmd.exe -ErrorAction SilentlyContinue)
    } elseif ($IsMacOS) { $script:EmperorOs = 'macos' }
    else { $script:EmperorOs = 'linux' }
}
try {
    [Console]::OutputEncoding = [System.Text.UTF8Encoding]::new($false)
    $OutputEncoding = [Console]::OutputEncoding
} catch {}
if (-not $env:EMPEROR_ENCODING) { $env:EMPEROR_ENCODING = 'UTF-8' }

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
