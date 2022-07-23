<?php

$inputs = getInputs();

//ここから入れかえる
[$La, $Ra, $Lb, $Rb] = explode(' ', trim($inputs[0]));

$cnt = 0;
for ($i = 0; $i <= 100; $i++) {
  if ($La <= $i && $i <= $Ra && $Lb <= $i && $i <= $Rb) {
    $cnt++;
  }
}
echo $cnt;


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
