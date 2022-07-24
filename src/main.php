<?php

$inputs = getInputs();

//ここから入れかえる
[$n, $m] = explode(' ', trim($inputs[0]));
$x = explode(' ', trim($inputs[1]));
$b = array();
for ($i = 1; $i <= $m; $i++) {
  [$c, $y] = explode(' ', trim($inputs[$i + 1]));
  $b[$c] = $y;
}

$score = array();
$score[0][0] = 0;
$bkMax = 0;
for ($i = 1; $i <= $n; $i++) {
  $max = 0;
  if ($i > 1) {
    $max = $bkMax;
  }
  $bkMax = 0;
  for ($j = 0; $j <= $n; $j++) {
    if ($j === 0) {
      $score[$i][$j] = $max;
    } else {
      $bonus = 0;
      if (!empty($b[$j])) {
        $bonus = $b[$j];
      }
      $score[$i][$j] = $score[$i - 1][$j - 1] + $x[($i - 1)] + $bonus;
    }
    if ($score[$i][$j] > $bkMax) {
      $bkMax = $score[$i][$j];
    }
  }
}

$ans = max($score[$n]);

echo $ans;

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
