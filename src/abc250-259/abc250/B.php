<?php
[$n, $a, $b] = explode(' ', trim(fgets(STDIN)));

$row = $n * $a;
$col = $n * $b;

for ($i = 0; $i < $row; $i++) {
  for ($j = 0; $j < $col; $j++) {
    $attribute = floor(($i / $a)) + floor(($j / $b));
    if ($attribute % 2 === 0) {
      echo ".";
    } else {
      echo "#";
    }
  }
  echo "\n";
}
