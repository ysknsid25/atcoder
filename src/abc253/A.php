<?php

$inputs = explode(' ', trim(fgets(STDIN)));
$b = $inputs[1];
$midVal =  median($inputs);

if ($midVal == $b) {
  echo "Yes";
} else {
  echo "No";
}

function median($list)
{
  sort($list);
  if (count($list) % 2 == 0) {
    return (($list[(count($list) / 2) - 1] + $list[((count($list) / 2))]) / 2);
  } else {
    return ($list[floor(count($list) / 2)]);
  }
}
