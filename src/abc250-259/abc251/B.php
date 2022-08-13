<?php

[$n, $w] = explode(' ', trim(fgets(STDIN)));
$inputs = explode(' ', trim(fgets(STDIN)));

$resultArr = array();

$i = 0;
while ($i < $n) {
  $inti = $inputs[$i];
  if ($inti <= $w) {
    $resultArr[$inti] = 1;
  }
  $j = $i + 1;
  while ($j < $n) {
    $intj = $inputs[$j];
    $googint = $inti + $intj;
    if ($googint <= $w) {
      $resultArr[$googint] = 1;
    }
    $k = $j + 1;
    while ($k < $n) {
      if ($j != $i && $j != $k && $i != $k) {
        $googint = $inti + $intj + $inputs[$k];
        if ($googint <= $w) {
          $resultArr[$googint] = 1;
        }
      }
      ++$k;
    }
    ++$j;
  }
  ++$i;
}

echo array_sum($resultArr);
