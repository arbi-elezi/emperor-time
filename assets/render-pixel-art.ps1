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
# blade: big symmetric spade, smooth curve to a centered point, planted upright
$blade = @{
    33=@(18,24);34=@(16,26);35=@(14,27);36=@(13,28);37=@(12,28);38=@(12,29);39=@(11,29)
    40=@(11,29);41=@(11,29);42=@(11,28);43=@(12,28);44=@(12,27);45=@(13,26);46=@(13,25)
    47=@(14,24);48=@(15,23);49=@(16,21);50=@(17,20);51=@(18,19)
}
foreach ($br in ($blade.Keys | Sort-Object)) {
    $Lb = $blade[$br][0]; $Rb = $blade[$br][1]
    $body = ''
    for ($bc = $Lb + 1; $bc -le $Rb - 1; $bc++) {
        if ($br -ge 35 -and $br -le 44 -and $bc -le ($Lb + 2)) { $body += 'h' }
        elseif ($bc -ge ($Rb - 2)) { $body += 'S' }
        else { $body += 's' }
    }
    Overlay $sh $br $Lb ('k' + $body + 'k')
}
# mound: row -> left,right of outline; drawn over blade's right side (mound in front)
$mound = @{
    26=@(37,40);27=@(35,42);28=@(33,44);29=@(32,45);30=@(31,47);31=@(30,49);32=@(29,51)
    33=@(28,53);34=@(28,54);35=@(29,55);36=@(29,56);37=@(29,57);38=@(28,58);39=@(28,58)
    40=@(28,59);41=@(28,59);42=@(27,60);43=@(27,60);44=@(26,61);45=@(25,61);46=@(24,61)
    47=@(24,62);48=@(23,62);49=@(22,62);50=@(22,62);51=@(22,62)
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
$ox = 17.0; $oy = 11.5                    # eye opening radii (bigger; almond bottom)
$irx = 9.5; $iry = 12.5                   # iris radii (taller than opening -> lid crops it)

for ($y = 0; $y -lt $EH; $y++) {
    for ($x = 0; $x -lt $EW; $x++) {
        $ch = 'f'
        foreach ($e in $eyes) {
            $side = 1.0; if ($e[0] -gt 56) { $side = -1.0 }   # +1 = toward nose (inner)
            $dxp = ($x - $e[0]); $rdy = ($y - $e[1])
            $dx = $dxp / $ox
            $dyn = $rdy / $oy
            if ($rdy -gt 0) { $dyn = $dyn * 1.30 }            # flatter lower curve -> almond
            $t = [math]::Sqrt($dx * $dx + $dyn * $dyn)
            if ($t -gt 1.22) { continue }
            $ipx = ($dxp * $side) / $ox                        # -1 outer .. +1 inner
            $lidY = -0.80 + 0.50 * $ipx                        # angry slant: pressed down toward nose
            $idx = $dxp / $irx; $idy = $rdy / $iry
            $it = [math]::Sqrt($idx * $idx + $idy * $idy)
            if ($t -le 1.10 -and $dyn -ge $lidY -and $dyn -lt ($lidY + 0.24)) { $ch = 'k' }          # thin slanted upper lid
            elseif ($t -le 1.10 -and $dyn -lt $lidY) { $ch = 'F' }                                   # brow shadow above the glare
            elseif ($t -gt 0.94 -and $t -le 1.04 -and $dyn -gt 0.38) { $ch = 'q' }                   # thin lower lash
            elseif ($dyn -ge ($lidY + 0.24)) {
                if ($it -le 1.0 -and $t -le 1.04) {
                    $ang = [math]::Atan2($idy, $idx)
                    if ($it -gt 0.78) { $ch = 'c' }
                    elseif ($it -gt 0.52) {
                        if (([math]::Floor(($ang + 3.2) * 4.45) % 2) -eq 0) { $ch = 'p' } else { $ch = 'P' }  # radial spokes
                    }
                    elseif ($it -gt 0.18) { $ch = 'r' }        # wide burning field
                    else { $ch = 'u' }                         # small furious pupil
                    $gx = $x - ($e[0] - 2); $gy = $y - ($e[1] - 5.5)
                    if (([math]::Abs($gx) + [math]::Abs($gy)) -le 2.4) { $ch = 'h' }     # star glint
                    if (($gx -eq 0 -and [math]::Abs($gy) -le 3) -or ($gy -eq 0 -and [math]::Abs($gx) -le 3)) { $ch = 'h' }
                    $sx = $x - ($e[0] + 4); $sy = $y - ($e[1] + 4.0)
                    if (($sx * $sx + $sy * $sy) -le 1.1) { $ch = 'o' }                   # warm sparkle
                }
                elseif ($t -le 1.02) {
                    if ($dyn -lt ($lidY + 0.46)) { $ch = 'N' } else { $ch = 'n' }        # sclera, shadowed at lid
                }
                elseif ($t -le 1.20 -and $dyn -gt 0.50) { if ($ch -eq 'f') { $ch = 'F' } }
            }
        }
        $ey[$y][$x] = $ch
    }
}
# hair: fills the whole frame around the eyes (no dark corners, no bare oval)
function HairColor([int]$hx, [int]$hy) {
    $hc = 'y'
    if (((($hx + 2 * $hy) % 13) + 13) % 13 -lt 2) { $hc = 'g' }
    elseif (((($hx - 3 * $hy) % 19) + 19) % 19 -lt 1) { $hc = 'Y' }
    return $hc
}
# deep wavy fringe across the top
for ($x = 0; $x -lt $EW; $x++) {
    $depth = 12 + [math]::Round(4 * [math]::Sin(0.16 * $x + 1.2))
    for ($y = 0; $y -lt $depth; $y++) { $ey[$y][$x] = (HairColor $x $y) }
}
# wide side locks framing the face, full height
for ($y = 0; $y -lt $EH; $y++) {
    $hwL = 12 - [math]::Floor($y * 0.18)
    for ($x = 0; $x -lt $hwL; $x++) { $ey[$y][$x] = (HairColor $x $y) }
    for ($x = 111; $x -gt (111 - $hwL); $x--) { $ey[$y][$x] = (HairColor $x $y) }
}
# sheared tapering strands, dense fringe (short over the irises, long elsewhere)
$strands = @(
    @(4,16,-0.5,3), @(9,14,0.5,2), @(14,18,0.4,3), @(24,12,0.5,2), @(34,10,-0.45,2),
    @(39,11,-0.5,2), @(44,15,0.55,3), @(50,13,0.45,2), @(55,20,0.3,3), @(61,12,-0.4,2),
    @(66,14,-0.5,3), @(71,13,0.5,2), @(77,10,0.45,2), @(83,9,-0.45,2), @(87,12,-0.4,2),
    @(92,11,0.4,2), @(97,17,0.5,3), @(107,15,-0.45,3)
)
foreach ($st in $strands) {
    $bx = $st[0]; $len = $st[1]; $slope = $st[2]; $hw0 = $st[3]
    $db = 10 + [math]::Round(4 * [math]::Sin(0.16 * $bx + 1.2)) - 2
    for ($d = 0; $d -le $len; $d++) {
        $yy = $db + $d
        if ($yy -ge $EH) { break }
        $cx = $bx + [math]::Round($d * $slope)
        $hw = [math]::Round($hw0 * (1.0 - ($d / [double]$len)))
        if ($hw -lt 0) { $hw = 0 }
        for ($xx = $cx - $hw; $xx -le $cx + $hw; $xx++) {
            if ($xx -lt 0 -or $xx -ge $EW) { continue }
            $ch = 'y'
            if ($hw -gt 0 -and $xx -eq ($cx + $hw)) { $ch = 'g' }   # shadow edge on one side only
            $ey[$yy][$xx] = $ch
        }
    }
}
# tiny nose hint
$ey[45][54] = 'F'; $ey[46][55] = 'F'

Render $ey $palE (Join-Path $PSScriptRoot 'scarlet-eyes.png') $Scale

# ---------------- CROSSED SHOVELS CREST (76 x 58, transparent, jolly-roger) ----------------
# Each shovel is drawn in its own rotated frame: u = along the 45-degree axis
# (grip at negative u, blade tip at max u), v = perpendicular. True diagonals,
# real spade blades - no axis-aligned compromises.
function ShovelChar([double]$u, [double]$v) {
    $gu = $u + 5.5   # grip: chunky D-block perpendicular to the shaft, rimmed hole
    if ([math]::Abs($gu) -le 3.8 -and [math]::Abs($v) -le 4.6) {
        if ([math]::Abs($gu) -le 1.0 -and [math]::Abs($v) -le 1.5) { return $null }
        if ([math]::Abs($gu) -le 1.8 -and [math]::Abs($v) -le 2.3) { return 'k' }
        if ([math]::Abs($gu) -ge 2.8 -or [math]::Abs($v) -ge 3.6) { return 'k' }
        return 'w'
    }
    if ($u -gt -2 -and $u -le 30) {   # shaft: 3px wood core, 1px outline
        $av = [math]::Abs($v)
        if ($av -le 1.6) { if ($v -gt 0.4) { return 'W' } else { return 'w' } }
        if ($av -le 2.8) { return 'k' }
        return $null
    }
    $bu = $u - 30                     # blade: broad spade - shoulder ears, near-parallel sides, blunt point
    if ($bu -ge 0 -and $bu -le 16.0) {
        if ($bu -lt 1.3) { $hw = 8.6 }                                   # foot-rest ears at the socket
        elseif ($bu -lt 9.5) { $hw = 7.5 - 1.0 * (($bu - 1.3) / 8.2) }   # near-parallel sides
        else {
            $tt = ($bu - 9.5) / 6.5
            if ($tt -gt 1) { $tt = 1 }
            $hw = 6.5 * [math]::Pow(1.0 - $tt, 0.65)                     # blunt rounded point
        }
        if ($hw -lt 0.7) { $hw = 0.7 }
        $av = [math]::Abs($v)
        if ($av -le $hw) {
            if ($av -gt ($hw - 1.5) -or $bu -gt 15.0 -or $bu -lt 1.0) { return 'k' }
            if ($v -gt ($hw * 0.30)) { return 'S' }
            if ($v -lt (-$hw * 0.45)) { return 'h' }
            return 's'
        }
        return $null
    }
    return $null
}
$CW = 76; $CH = 58
$cr = New-Grid $CW $CH
$rt2 = [math]::Sqrt(2.0)
for ($y = 0; $y -lt $CH; $y++) {
    for ($x = 0; $x -lt $CW; $x++) {
        $uA = (($x - 21) + ($y - 15)) / $rt2; $vA = (($x - 21) - ($y - 15)) / $rt2
        $cA = ShovelChar $uA $vA
        $uB = ((55 - $x) + ($y - 15)) / $rt2; $vB = ((55 - $x) - ($y - 15)) / $rt2
        $cB = ShovelChar $uB $vB
        $cc = $cA
        if ($null -ne $cB) { $cc = $cB }   # right shovel crosses in front
        if ($null -ne $cc) { $cr[$y][$x] = $cc }
    }
}
Render $cr $palS (Join-Path $PSScriptRoot 'crossed-shovels.png') $Scale
