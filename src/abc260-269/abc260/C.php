<?php

fscanf(STDIN, "%d %d %d", $N, $X, $Y);

$Rarr = array();
$Barr = array();

for ($i = 1; $i < 11; $i++) {
  $Rarr[$i] = 0;
  $Barr[$i] = 0;
}

$Rarr[$N] = 1;

for ($i = $N; $i >= 2; $i--) {
  $Rarr[$i - 1] += $Rarr[$i];
  $Barr[$i] += $Rarr[$i] * $X;

  $Rarr[$i - 1] += $Barr[$i];
  $Barr[$i - 1] += $Barr[$i] * $Y;
}

echo $Barr[1];
