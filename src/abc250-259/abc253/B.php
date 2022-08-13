<?php

[$h, $w] = explode(' ', trim(fgets(STDIN)));

$rowInfo = array();
$colInfo = array();
for ($i = 0; $i < $h; $i++) {
  $word = str_replace(array("\r\n", "\r", "\n"), "", fgets(STDIN));
  $strarr = str_split($word);
  for ($j = 0; $j < count($strarr); $j++) {
    $char = $strarr[$j];
    if ("o" == $char) {
      $rowInfo[] = $i;
      $colInfo[] = $j;
    }
  }
}

$from_i = $rowInfo[0];
$from_j = $colInfo[0];

$to_i = $rowInfo[1];
$to_j = $colInfo[1];

$dist_i = abs(($from_i - $to_i));
$dist_j = abs(($from_j - $to_j));

$dist = $dist_i + $dist_j;
echo $dist;
