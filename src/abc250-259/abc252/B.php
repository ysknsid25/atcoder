<?php

[$n, $k] = explode(' ', fgets(STDIN));
$foods = explode(' ', trim(fgets(STDIN)));
$dislikes = explode(' ', trim(fgets(STDIN)));

arsort($foods);
$maxvalue = max($foods);
$keys = array_keys($foods, $maxvalue);

$hasDislike = "No";
foreach ($keys as $key) {
  $disLikeKey = $key + 1;
  $result = array_search($disLikeKey, $dislikes);
  if ($result !== false) {
    $hasDislike = "Yes";
    break;
  }
}

echo $hasDislike;
