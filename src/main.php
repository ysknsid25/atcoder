<?php

$inputs = getInputs();

$n = $inputs[0];

$cntArr = array();
for ($i = 1; $i <= $n; $i++) {
  $word = str_replace(array("\r\n", "\r", "\n"), "", $inputs[$i]);
  if (empty($cntArr[$word])) {
    $cntArr[$word] = 1;
  } else {
    $cntArr[$word] += 1;
  }
  if ($cntArr[$word] === 1) {
    echo $word . "\n";
  } else {
    echo $word . "(" . ($i - 1) . ")" . "\n";
  }
}


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
