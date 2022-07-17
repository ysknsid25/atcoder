<?php
//https://atcoder.jp/contests/abc259/tasks/abc259_a
fscanf(STDIN, "%d %d %d %d %d", $N, $M, $X, $T, $D);

$height = $T;
if (0 <= $M && $M < $X) {
  $ageDiff = $X - $M;
  $height = $T - ($ageDiff * $D);
}
echo $height;
