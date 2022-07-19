<?php

$inputs = getInputs();

[$n] = explode(' ', trim($inputs[0]));
$integers = explode(' ', trim($inputs[1]));

$komaExistsArr = array();

$p = 0;
for ($i = 0; $i < count($integers); $i++) {
  $komaExistsArr[0] = true;
  $add = $integers[$i];
  for ($j = 3; $j > -1; $j--) {
    if (empty($komaExistsArr[$j])) {
      continue;
    }
    $isExists = $komaExistsArr[$j];
    $posi = $j;
    if ($isExists) {
      $newPosi = $posi + $add;
      if ($newPosi > 3) {
        $p++;
      } else {
        $komaExistsArr[$newPosi] = true;
      }
      $komaExistsArr[$posi] = false;
    }
  }
}

echo $p;

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
