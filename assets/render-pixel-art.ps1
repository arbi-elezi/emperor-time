# Renders the README pixel art (shovel + scarlet eyes) as PNGs.
# Windows PowerShell 5.1+ (System.Drawing). Output: assets/shovel.png, assets/scarlet-eyes.png
param([int]$Scale = 8)
$ErrorActionPreference = 'Stop'
Add-Type -AssemblyName System.Drawing

function New-Grid([int]$W, [int]$H) {
    $g = New-Object 'System.Collections.Generic.List[char[]]'
    for ($i = 0; $i -lt $H; $i++) { $g.Add(('.' * $W).ToCharArray()) }
    return ,$g   # comma prevents pipeline unrolling into a flat char stream
}
function Overlay($grid, [int]$row, [int]$col, [string]$s) {
    if ($null -eq $grid -or $null -eq $grid[$row]) {
        throw ("Overlay diagnostic: row={0} col={1} s='{2}' gridType={3} gridCount={4}" -f $row, $col, $s, $(if ($null -eq $grid) { 'NULL' } else { $grid.GetType().Name }), $(if ($null -eq $grid) { -1 } else { $grid.Count }))
    }
    if ($col -lt 0 -or ($col + $s.Length) -gt $grid[$row].Count) {
        throw ("Overlay out of bounds: row={0} col={1} len={2} width={3} s='{4}'" -f $row, $col, $s.Length, $grid[$row].Count, $s)
    }
    for ($i = 0; $i -lt $s.Length; $i++) { $grid[$row][$col + $i] = $s[$i] }
}
function Render($grid, $palette, [string]$path, [int]$scale) {
    $H = $grid.Count; $W = $grid[0].Count
    $small = New-Object System.Drawing.Bitmap($W, $H, [System.Drawing.Imaging.PixelFormat]::Format32bppArgb)
    for ($y = 0; $y -lt $H; $y++) {
        for ($x = 0; $x -lt $W; $x++) {
            $ch = [string]$grid[$y][$x]
            if ($ch -ne '.') { $small.SetPixel($x, $y, $palette[$ch]) }
        }
    }
    $big = New-Object System.Drawing.Bitmap(($W * $scale), ($H * $scale))
    $gr = [System.Drawing.Graphics]::FromImage($big)
    $gr.InterpolationMode = [System.Drawing.Drawing2D.InterpolationMode]::NearestNeighbor
    $gr.PixelOffsetMode = [System.Drawing.Drawing2D.PixelOffsetMode]::Half
    $gr.DrawImage($small, 0, 0, $W * $scale, $H * $scale)
    $gr.Dispose()
    $big.Save($path, [System.Drawing.Imaging.ImageFormat]::Png)
    $big.Dispose(); $small.Dispose()
    Write-Host ("rendered {0} ({1}x{2} logical, {3}x{4} px)" -f $path, $W, $H, ($W*$scale), ($H*$scale))
}
function C([string]$hex) { [System.Drawing.ColorTranslator]::FromHtml($hex) }

# ---------------- SHOVEL (64 x 56, transparent bg) ----------------
# case-sensitive palette (@{} literals fold 'w'/'W' together)
$palS = New-Object System.Collections.Hashtable
$palS['k'] = C '#1c1c1c'   # outline
$palS['w'] = C '#c08a50'   # wood light
$palS['W'] = C '#96602f'   # wood shade
$palS['s'] = C '#9aa8b2'   # steel
$palS['S'] = C '#67737d'   # steel shade
$palS['h'] = C '#ccd6dc'   # steel highlight
$palS['d'] = C '#6b482a'   # dirt
$palS['D'] = C '#452c15'   # dirt dark squiggle
$palS['m'] = C '#8f6236'   # dirt light
$palS['r'] = C '#e0402c'   # red fleck
$palS['o'] = C '#e08030'   # orange fleck
$sh = New-Grid 64 56
# D-grip
Overlay $sh 1 12 'kkkkkkkk'
Overlay $sh 2 10 'kk'; Overlay $sh 2 12 'wwwwwwww'; Overlay $sh 2 20 'kk'
Overlay $sh 3 9 'k'; Overlay $sh 3 10 'wwwwwwwwww'; Overlay $sh 3 20 'W'; Overlay $sh 3 21 'k'
foreach ($r in 4..8) { Overlay $sh $r 9 'kwwk'; Overlay $sh $r 19 'kwWk' }
Overlay $sh 9 9 'k'; Overlay $sh 9 10 'ww'; Overlay $sh 9 12 'kkkkkkkk'; Overlay $sh 9 20 'wW'; Overlay $sh 9 22 'k'
Overlay $sh 10 9 'k'; Overlay $sh 10 10 'wwwww'; Overlay $sh 10 15 'WWWWWW'; Overlay $sh 10 21 'k'
Overlay $sh 11 10 'k'; Overlay $sh 11 11 'wwww'; Overlay $sh 11 15 'WWWWW'; Overlay $sh 11 20 'k'
Overlay $sh 12 12 'k'; Overlay $sh 12 13 'www'; Overlay $sh 12 16 'WW'; Overlay $sh 12 18 'k'
# shaft (leans right)
foreach ($r in 13..15) { Overlay $sh $r 14 'k'; Overlay $sh $r 15 'ww'; Overlay $sh $r 17 'W'; Overlay $sh $r 18 'k' }
foreach ($r in 16..19) { Overlay $sh $r 15 'k'; Overlay $sh $r 16 'ww'; Overlay $sh $r 18 'W'; Overlay $sh $r 19 'k' }
foreach ($r in 20..23) { Overlay $sh $r 16 'k'; Overlay $sh $r 17 'ww'; Overlay $sh $r 19 'W'; Overlay $sh $r 20 'k' }
foreach ($r in 24..27) { Overlay $sh $r 17 'k'; Overlay $sh $r 18 'ww'; Overlay $sh $r 20 'W'; Overlay $sh $r 21 'k' }
foreach ($r in 28..31) { Overlay $sh $r 18 'k'; Overlay $sh $r 19 'ww'; Overlay $sh $r 21 'W'; Overlay $sh $r 22 'k' }
Overlay $sh 32 19 'k'; Overlay $sh 32 20 'ww'; Overlay $sh 32 22 'W'; Overlay $sh 32 23 'k'
# blade: smooth rounded spade, tip drifting slightly left, planted
Overlay $sh 33 18 'k'; Overlay $sh 33 19 'sss'; Overlay $sh 33 22 'S'; Overlay $sh 33 23 'k'
$blade = @{
    34=@(16,24);35=@(14,25);36=@(13,26);37=@(12,26);38=@(12,27);39=@(11,27);40=@(11,27)
    41=@(11,26);42=@(12,26);43=@(12,25);44=@(12,25);45=@(13,24);46=@(13,23);47=@(14,22)
    48=@(14,20);49=@(15,19);50=@(16,18)
}
foreach ($br in ($blade.Keys | Sort-Object)) {
    $Lb = $blade[$br][0]; $Rb = $blade[$br][1]
    $body = ''
    for ($bc = $Lb + 1; $bc -le $Rb - 1; $bc++) {
        if ($br -ge 35 -and $br -le 40 -and $bc -le ($Lb + 2)) { $body += 'h' }
        elseif ($bc -ge ($Rb - 2)) { $body += 'S' }
        else { $body += 's' }
    }
    Overlay $sh $br $Lb ('k' + $body + 'k')
}
Overlay $sh 51 16 'kk'
# mound: row -> left,right of outline; drawn over blade's right side (mound in front)
$mound = @{
    26=@(37,40);27=@(35,42);28=@(33,44);29=@(32,45);30=@(31,47);31=@(30,49);32=@(29,51)
    33=@(28,53);34=@(27,54);35=@(26,55);36=@(26,56);37=@(27,57);38=@(26,58);39=@(25,58)
    40=@(27,59);41=@(26,59);42=@(25,60);43=@(24,60);44=@(24,61);45=@(23,61);46=@(22,61)
    47=@(23,62);48=@(23,62);49=@(22,62);50=@(22,62);51=@(22,62)
}
foreach ($mr in ($mound.Keys | Sort-Object)) {
    # NB: PS variables are case-insensitive — $R would clobber a $r loop var
    $Lx = $mound[$mr][0]; $Rx = $mound[$mr][1]
    Overlay $sh $mr $Lx ('k' + ('d' * ($Rx - $Lx - 1)) + 'k')
}
# dirt texture: dark squiggles, light spots, red/orange flecks
$flecks = @{
    28=@(,@(39,'r'));29=@(,@(36,'DD'));30=@(,@(43,'o'));31=@(@(33,'r'),@(45,'D'))
    32=@(@(38,'DD'),@(48,'o'));33=@(@(31,'m'),@(42,'r'));34=@(@(36,'o'),@(50,'DD'))
    35=@(@(29,'r'),@(46,'D'),@(33,'m'));36=@(@(39,'DD'),@(52,'r'))
    37=@(@(31,'o'),@(44,'r'),@(54,'m'));38=@(@(36,'D'),@(49,'o'))
    39=@(@(29,'r'),@(41,'DD'),@(55,'r'));40=@(@(33,'o'),@(46,'m'),@(52,'D'))
    41=@(@(38,'r'),@(57,'o'));42=@(@(30,'DD'),@(43,'o'),@(50,'r'))
    43=@(@(35,'r'),@(54,'DD'));44=@(@(28,'o'),@(40,'D'),@(47,'r'),@(58,'m'))
    45=@(@(32,'r'),@(51,'o'));46=@(@(37,'DD'),@(44,'r'),@(56,'D'))
    47=@(@(29,'m'),@(48,'o'));48=@(@(34,'r'),@(41,'o'),@(53,'DD'))
    49=@(@(27,'D'),@(45,'r'),@(58,'o'));50=@(@(31,'o'),@(38,'m'),@(49,'D'))
    51=@(,@(42,'r'))
}
foreach ($r in $flecks.Keys) { foreach ($f in $flecks[$r]) { Overlay $sh $r $f[0] $f[1] } }
# clods + ground specks
Overlay $sh 47 8 'k'; Overlay $sh 47 9 'd'; Overlay $sh 47 10 'k'
Overlay $sh 48 7 'k'; Overlay $sh 48 8 'dd'; Overlay $sh 48 10 'k'
Overlay $sh 49 6 'kdddk'
Overlay $sh 50 7 'kddk'; Overlay $sh 50 16 'kdk'; Overlay $sh 50 3 'k'
Overlay $sh 51 8 'kk'; Overlay $sh 51 15 'kddk'
Overlay $sh 53 5 'kkk'; Overlay $sh 53 12 'kkk'; Overlay $sh 53 20 'kkkk'; Overlay $sh 53 30 'kkkk'
Overlay $sh 53 41 'kkkk'; Overlay $sh 53 52 'kkkk'; Overlay $sh 53 60 'kk'
Overlay $sh 54 9 'k'; Overlay $sh 54 17 'k'; Overlay $sh 54 27 'k'; Overlay $sh 54 37 'k'; Overlay $sh 54 48 'k'; Overlay $sh 54 58 'k'

Render $sh $palS (Join-Path $PSScriptRoot 'shovel.png') $Scale

# ---------------- SCARLET EYES (112 x 48, full-bleed, procedural) ----------------
$palE = New-Object System.Collections.Hashtable
$palE['k'] = C '#141018'   # lids / bg corners
$palE['q'] = C '#4a1a26'   # lower lid maroon
$palE['y'] = C '#cfc06e'   # hair
$palE['Y'] = C '#e8dc8e'   # hair highlight
$palE['g'] = C '#8f9c55'   # hair olive streak
$palE['G'] = C '#5c6f3c'   # hair dark streak
$palE['f'] = C '#e9e3f0'   # skin
$palE['F'] = C '#c9c1da'   # skin shadow
$palE['n'] = C '#f5f1f8'   # sclera
$palE['N'] = C '#d8d2e6'   # sclera shadow under lid
$palE['c'] = C '#8e1c2c'   # iris outer crimson
$palE['p'] = C '#e0507c'   # iris pink ring
$palE['P'] = C '#f6a2be'   # iris pink spoke
$palE['r'] = C '#c02034'   # iris red field
$palE['u'] = C '#3c0e16'   # pupil
$palE['h'] = C '#ffffff'   # glint
$palE['o'] = C '#ff9668'   # warm sparkle
$EW = 112; $EH = 48
$ey = New-Grid $EW $EH
$eyes = @(@(30.0, 29.0), @(82.0, 29.0))   # centers
$ox = 15.0; $oy = 10.5                    # eye opening radii (almond: bottom pulled flatter)
$irx = 8.2; $iry = 11.2                   # iris radii (taller than opening -> lids crop it)

for ($y = 0; $y -lt $EH; $y++) {
    for ($x = 0; $x -lt $EW; $x++) {
        $ch = 'f'
        foreach ($e in $eyes) {
            $rdy = ($y - $e[1])
            $dx = ($x - $e[0]) / $ox
            $dyn = $rdy / $oy
            if ($rdy -gt 0) { $dyn = $dyn * 1.28 }   # flatter lower curve -> almond, not circle
            $t = [math]::Sqrt($dx * $dx + $dyn * $dyn)
            if ($t -le 1.22) {
                $idx = ($x - $e[0]) / $irx; $idy = $rdy / $iry
                $it = [math]::Sqrt($idx * $idx + $idy * $idy)
                if ($t -gt 0.76 -and $t -le 1.10 -and $rdy -lt (-0.18 * $oy)) { $ch = 'k' }          # upper lid: thick top arc only
                elseif ($t -gt 0.94 -and $t -le 1.10 -and $rdy -lt (0.10 * $oy)) { $ch = 'k' }       # lid tapers toward corners
                elseif ($t -gt 0.92 -and $t -le 1.06 -and $rdy -gt (0.30 * $oy)) { $ch = 'q' }       # lower lid: thin
                elseif ($it -le 1.0 -and $t -le 1.02) {
                    $ang = [math]::Atan2($idy, $idx)
                    if ($it -gt 0.80) { $ch = 'c' }
                    elseif ($it -gt 0.56) {
                        if (([math]::Floor(($ang + 3.2) * 4.45) % 2) -eq 0) { $ch = 'p' } else { $ch = 'P' }  # radial spokes
                    }
                    elseif ($it -gt 0.34) { $ch = 'r' }
                    else { $ch = 'u' }
                    $gx = $x - ($e[0] - 2); $gy = $y - ($e[1] - 5.0)
                    if (([math]::Abs($gx) + [math]::Abs($gy)) -le 2.8) { $ch = 'h' }     # four-point star glint
                    if (($gx -eq 0 -and [math]::Abs($gy) -le 4) -or ($gy -eq 0 -and [math]::Abs($gx) -le 4)) { $ch = 'h' }  # star rays
                    $sx = $x - ($e[0] + 4); $sy = $y - ($e[1] + 3.5)
                    if (($sx * $sx + $sy * $sy) -le 1.1) { $ch = 'o' }                   # warm sparkle
                }
                elseif ($t -le 1.02) {
                    if ($rdy -lt (-0.30 * $oy)) { $ch = 'N' } else { $ch = 'n' }         # sclera (shadowed under lid)
                }
                elseif ($t -le 1.20 -and $rdy -gt (0.50 * $oy)) { if ($ch -eq 'f') { $ch = 'F' } }   # soft under-eye shade
            }
        }
        $ey[$y][$x] = $ch
    }
}
# hair: wavy base band with diagonal streaks, then sheared tapering strands
# (drawn OVER lids like the reference; slanted swooshes, not icicles)
for ($x = 0; $x -lt $EW; $x++) {
    $depth = 8 + [math]::Round(3 * [math]::Sin(0.16 * $x + 1.2))
    for ($y = 0; $y -lt $depth; $y++) {
        $ch = 'y'
        if (((($x + 2 * $y) % 9) + 9) % 9 -lt 2) { $ch = 'g' }
        elseif (((($x - 3 * $y) % 13) + 13) % 13 -lt 1) { $ch = 'Y' }
        $ey[$y][$x] = $ch
    }
}
# strands: baseX, length, slope (shear per step), starting half-width
$strands = @(
    @(5,11,-0.5,2), @(17,14,0.45,3), @(29,9,-0.4,2), @(42,12,0.5,3), @(54,16,0.35,3),
    @(67,11,-0.45,2), @(79,14,0.5,3), @(92,10,-0.4,2), @(102,12,0.45,2)
)
foreach ($st in $strands) {
    $bx = $st[0]; $len = $st[1]; $slope = $st[2]; $hw0 = $st[3]
    $db = 6 + [math]::Round(3 * [math]::Sin(0.16 * $bx + 1.2))
    for ($d = 0; $d -le $len; $d++) {
        $yy = $db + $d
        if ($yy -ge $EH) { break }
        $cx = $bx + [math]::Round($d * $slope)
        $hw = [math]::Round($hw0 * (1.0 - ($d / [double]$len)))
        if ($hw -lt 0) { $hw = 0 }
        for ($xx = $cx - $hw; $xx -le $cx + $hw; $xx++) {
            if ($xx -lt 0 -or $xx -ge $EW) { continue }
            $ch = 'y'
            if ($xx -eq ($cx - $hw) -or $xx -eq ($cx + $hw)) { $ch = 'g' }
            if ($d % 4 -eq 0 -and $hw -gt 0 -and $xx -eq $cx) { $ch = 'Y' }
            $ey[$yy][$xx] = $ch
        }
    }
}
# side hair: tapering locks
for ($y = 0; $y -lt 28; $y++) {
    $hw = 3 - [math]::Floor($y / 10)
    for ($x = 0; $x -lt $hw; $x++) { $c2 = 'y'; if ($x -eq ($hw - 1)) { $c2 = 'g' }; $ey[$y][$x] = $c2 }
    for ($x = 111; $x -gt (111 - $hw); $x--) { $c2 = 'y'; if ($x -eq (112 - $hw)) { $c2 = 'g' }; $ey[$y][$x] = $c2 }
}
# dark vignette corners
for ($y = 0; $y -lt 14; $y++) {
    for ($x = 0; $x -lt $EW; $x++) {
        if (($x -lt 14 -and $y -lt (12 - 0.9 * $x)) -or ($x -gt 97 -and $y -lt (12 - 0.9 * (111 - $x)))) { $ey[$y][$x] = 'k' }
    }
}
# tiny nose hint
$ey[45][54] = 'F'; $ey[46][55] = 'F'

Render $ey $palE (Join-Path $PSScriptRoot 'scarlet-eyes.png') $Scale
