# Dot-source only. Idempotent: wrap function defs so re-source is safe.
# Resolve Python launcher for Emperor thin .ps1 twins.
# Order: EMPEROR_PYTHON → python3 → py -3 → python.

if (-not (Get-Command Resolve-EmperorPython -ErrorAction SilentlyContinue)) {

function Resolve-EmperorPython {
    <#
    .SYNOPSIS
      Resolve the Python launcher for Emperor thin .ps1 twins.
    .OUTPUTS
      [pscustomobject] @{ Exe = [string]; PrefixArgs = [string[]] }
      Exe is a path or command name. PrefixArgs is @() for normal interpreters,
      or @('-3') when the Windows py launcher is selected.
    .NOTES
      Order: EMPEROR_PYTHON → python3 → py -3 → python.
      Throws a clear error if none are usable.
    #>
    $override = $env:EMPEROR_PYTHON
    if ($override -and $override.Trim().Length -gt 0) {
        $cand = $override.Trim()
        $usable = $false
        if ($cand -match '[\\/]' -or $cand -match '\.(exe|bat|cmd|ps1)$') {
            if (Test-Path -LiteralPath $cand) { $usable = $true }
        }
        if (-not $usable) {
            if (Get-Command $cand -ErrorAction SilentlyContinue) { $usable = $true }
        }
        if (-not $usable) {
            throw "emperor: EMPEROR_PYTHON is set but not usable: $cand"
        }
        return [pscustomobject]@{ Exe = $cand; PrefixArgs = @() }
    }

    if (Get-Command python3 -ErrorAction SilentlyContinue) {
        return [pscustomobject]@{ Exe = 'python3'; PrefixArgs = @() }
    }
    if (Get-Command py -ErrorAction SilentlyContinue) {
        return [pscustomobject]@{ Exe = 'py'; PrefixArgs = @('-3') }
    }
    if (Get-Command python -ErrorAction SilentlyContinue) {
        return [pscustomobject]@{ Exe = 'python'; PrefixArgs = @() }
    }

    throw 'emperor: no Python launcher (set EMPEROR_PYTHON, or install python3 / py -3 / python)'
}

function Invoke-EmperorPython {
    param(
        [Parameter(Mandatory = $true, Position = 0)]
        [string]$File,
        [Parameter(ValueFromRemainingArguments = $true)]
        [object[]]$ArgumentList
    )
    $r = Resolve-EmperorPython
    & $r.Exe @($r.PrefixArgs) $File @ArgumentList
    # leave $LASTEXITCODE for caller; do not wrap exit here
}

} # end idempotent guard
