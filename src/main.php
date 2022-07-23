<?php

$inputs = getInputs();

//ここから入れかえる

$a = array_fill(0, 3, array_fill(0, 2, 1));
var_dump($a);


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
