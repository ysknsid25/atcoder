<?php
//https://atcoder.jp/contests/abc259/tasks/abc259_b
fscanf(STDIN, "%d %d %d", $a, $b, $d);

$beforerad = atan2($b, $a);
$beforedeg = rad2deg($beforerad);
$afterDeg = $beforedeg + $d;
$afterRad = deg2rad($afterDeg);

$r = sqrt(($a * $a + $b * $b));

$x = cos($afterRad) * $r;
$y = sin($afterRad) * $r;

echo $x . ' ' . $y;
