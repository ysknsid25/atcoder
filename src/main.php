<?php

$inputs = getInputs();

$ninehour = date("h:i", strtotime('+100 minute', strtotime("21:00")));
echo $ninehour;

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
