<?php

$inputs = getInputs();

//ここから入れかえる

[$n, $k] = explode(' ', $inputs[0]);
$foods = explode(' ', trim($inputs[1]));
$dislikes = explode(' ', trim($inputs[2]));

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


//ここまで入れ替える

/**
 * テスト用にファイルからサンプルデータを受け取る
 */
function getInputs()
{
  $retArr = array();
  $file = fopen("sample.txt", "r");
  while ($line = fgets($file)) {
    $retArr[] = $line;
  }
  fclose($file);
  return $retArr;
}
