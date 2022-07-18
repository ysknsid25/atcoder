<?php

$inputs = getInputs();

[$n, $q] = explode(' ', trim($inputs[0]));
$s = str_replace(array("\r\n", "\r", "\n"), "", $inputs[1]);

$typeArr = array();
$targetArr = array();
for ($i = 0; $i < $q; $i++) {
  [$v, $x] = explode(' ', trim($inputs[($i + 2)]));
  if ($v == "1") {
    $s = execquery1($s, $x);
  } else {
    execquery2($s, $x);
  }
}

function execquery1($s, $x)
{
  $retStr = $s;
  $lastIndex = strlen($retStr);
  $strBeginPosi = $lastIndex - $x;

  $removedStr = substr($retStr, $strBeginPosi, $lastIndex);
  $remainStr = substr($retStr, 0, $strBeginPosi);
  $retStr = $removedStr . $remainStr;

  return $retStr;
}

function execquery2($s, $x)
{
  $beginPosi = $x - 1;
  $result = substr($s, $beginPosi, 1);
  echo $result . "\n";
}

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
