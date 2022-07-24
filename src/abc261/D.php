<?php

[$n, $m] = explode(' ', trim(fgets(STDIN)));
$x = explode(' ', trim(fgets(STDIN)));
$b = array();
for ($i = 1; $i <= $m; $i++) {
  [$c, $y] = explode(' ', trim(fgets(STDIN)));
  $b[$c] = $y;
}

$score = array_fill(0, ($n + 1), array_fill(0, ($n + 1), -1));
$score[0][0] = 0;
for ($i = 1; $i <= $n; $i++) {
  for ($j = 0; $j <= $i; $j++) {
    if ($j === 0) {
      $score[$i][$j] = max($score[$i - 1]);
    } else {
      $bonus = 0;
      if (!empty($b[$j])) {
        $bonus = $b[$j];
      }
      $score[$i][$j] = $score[$i - 1][$j - 1] + $x[($i - 1)] + $bonus;
    }
  }
}

$ans = max($score[$n]);

echo $ans;
