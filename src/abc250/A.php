<?php
[$h, $w] = explode(' ', trim(fgets(STDIN)));
[$r, $c] = explode(' ', trim(fgets(STDIN)));

$cnt = 0;
for ($i = 1; $i <= $h; $i++) {
  for ($j = 1; $j <= $w; $j++) {
    $dist = abs(($r - $i)) + abs(($c - $j));
    if ($dist === 1) {
      $cnt++;
    }
  }
}
echo $cnt;
