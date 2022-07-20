<?php

$inputs = getInputs();

//ここから入れかえる

[$n, $k] = explode(' ', trim($inputs[0]));
$inputs2 = explode(' ', trim($inputs[1]));

$haveLights = array();
foreach ($inputs2 as $index) {
  $who = $index - 1;
  $haveLights[] = $who;
}

$x = array();
$y = array();
for ($i = 0; $i < $n; $i++) {
  [$tmpx, $tmpy] = explode(' ', $inputs[($i + 2)]);
  $x[] = $tmpx;
  $y[] = $tmpy;
}

$r = array();
for ($i = 0; $i < $n; $i++) {
  $xposi = $x[$i];
  $yposi = $y[$i];
  $mindist = 1000000000000000000; //十分大きい数
  foreach ($haveLights as $who) {
    if ($i == $who) {
      $mindist = 0;
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

//ここまで入れ替える

/**
 * テスト用にファイルからサンプルデータを受け取る
 */
function getInputs()
{
  $retArr = array();
  $file = fopen("sample.txt", "r");
  while ($line = fgets($file)) {
    $retArr[] = $line;
  }
  fclose($file);
  return $retArr;
}
