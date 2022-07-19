<?php

fscanf(STDIN, "%d %d", $r, $c);
$inputs1 = explode(' ', trim(fgets(STDIN)));
$inputs2 = explode(' ', trim(fgets(STDIN)));

$arr[] = $inputs1;
$arr[] = $inputs2;

$rowIndex = $r - 1;
$colIndex = $c - 1;

echo $arr[$rowIndex][$colIndex];
