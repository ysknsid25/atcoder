<?php
//https://atcoder.jp/contests/abc259/tasks/abc259_c
$s = fgets(STDIN);
$t = fgets(STDIN);

$sArr = ranlength($s);
$tArr = ranlength($t);

$result = "Yes";
for ($i = 0; $i < count($tArr); $i++) {
  $tInfo = $tArr[$i];
  $sInfo = $sArr[$i];
  foreach ($tInfo as $char => $cnt) {
    if (empty($sInfo[$char])) {
      $result = "No";
      break 2;
    }
    if ($cnt > 1 && $sInfo[$char] < 2) {
      $result = "No";
      break 2;
    }
  }
}
echo $result;

function ranlength($word)
{
  $charArr = str_split(str_replace(array("\r\n", "\r", "\n"), "", $word));
  $bkchar = $charArr[0];
  $sameCount = 0;
  $lengthCharArr = array();
  foreach ($charArr as $char) {
    if ($bkchar != $char) {
      $tmpArr = array();
      $tmpArr[$bkchar] = $sameCount;
      $lengthCharArr[] = $tmpArr;
      $sameCount = 0;
    }
    $sameCount++;
    $bkchar = $char;
  }
  //最後の1文字
  $tmpArr = array();
  $tmpArr[$bkchar] = $sameCount;
  $lengthCharArr[] = $tmpArr;
  return $lengthCharArr;
}
