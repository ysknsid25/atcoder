<?php

fscanf(STDIN, "%d %d", $n, $q);
$s = str_replace(array("\r\n", "\r", "\n"), "", fgets(STDIN));

$typeArr = array();
$targetArr = array();
for ($i = 0; $i < $q; $i++) {
  fscanf(STDIN, "%d %d", $v, $x);
  if ($v == "1") {
    if ($n == $x) {
      continue;
    }
    $s = execquery1($s, (int)$x);
  } else {
    execquery2($s, (int)$x);
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
