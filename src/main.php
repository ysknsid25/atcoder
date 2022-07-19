<?php

$inputs = getInputs();

[$n, $k, $q] = explode(' ', trim($inputs[0]));
$initPosi = explode(' ', trim($inputs[1]));
$query = explode(' ', trim($inputs[2]));

$lastRight = $n - 1;

$komaExists = array();
$komaPosi = array();
for ($i = 1; $i < $n; $i++) {
  $posi = $initPosi[$i] - 1;
  $komaExists[$posi] = true;
  $komaPosi[] = $posi;
}

foreach ($query as $target) {
  $targetkoma = $target - 1;
  $posi = $komaPosi[$targetkoma];
  $nextPosi = $posi + 1;
  if ($posi == $lastRight) {
    continue;
  }
  $rightKomaExist = $komaExists[$nextPosi];
  if ($rightKomaExist) {
    continue;
  }
  $komaPosi[$targetkoma] = $nextPosi;
  $komaExists[$posi] = false;
  $komaExists[$nextPosi] = true;
}

$out = "";
foreach ($komaPosi as $posi) {
  $out = ($posi + 1) . " ";
}
echo substr($out, -1);

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
