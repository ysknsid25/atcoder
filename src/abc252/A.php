<?php

$aphaArr = [
  "a", "b", "c", "d", "e",
  "f", "g", "h", "i", "j",
  "k", "l", "m", "n", "o",
  "p", "q", "r", "s", "t",
  "u", "v", "w", "x", "y",
  "z"
];

$base = 97;
fscanf(STDIN, "%d", $n);

$index = $n - $base;

echo $aphaArr[$index];
