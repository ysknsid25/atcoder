<?php

[$n, $k] = explode(' ', trim(fgets(STDIN)));
$inputs = explode(' ', trim(fgets(STDIN)));

$haveLights = array();
foreach ($inputs as $index) {
  $who = $index - 1;
  $haveLights[] = $who;
}

$x = array();
$y = array();
for ($i = 0; $i < $n; $i++) {
  [$tmpx, $tmpy] = explode(' ', trim(fgets(STDIN)));
  $x[] = $tmpx;
  $y[] = $tmpy;
}

$r = array();
for ($i = 0; $i < $n; $i++) {
  $xposi = $x[$i];
  $yposi = $y[$i];
  $mindist = pow(10, 15); //十分大きい数
  foreach ($haveLights as $who) {
    if ($i == $who) {
      continue;
    }
    $lightx = $x[$who];
    $lighty = $y[$who];
    $dist = sqrt(pow(($lightx - $xposi), 2) + pow(($lighty - $yposi), 2));
    if ($dist < $mindist) {
      $mindist = $dist;
    }
  }
  $r[] = $mindist;
}

$result = max($r);

echo $result;
