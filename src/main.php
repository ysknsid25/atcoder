<?php

$inputs = getInputs();

[$N, $X, $Y, $Z] = explode(' ', trim($inputs[0]));
$mathscores = explode(' ', trim($inputs[1]));
$engscores = explode(' ', trim($inputs[2]));

$scoreArr = array();
for ($i = 0; $i < count($mathscores); $i++) {
  $mathscore = 0;
  if ($mathscores[$i] > 0) {
    $mathscore = $mathscores[$i];
  }
  $engscore = 0;
  if ($engscores[$i] > 0) {
    $engscore = $engscores[$i];
  }
  $totalscore = $mathscore + $engscore;
  $scoreArr["m"][$i] = (int)$mathscore;
  $scoreArr["e"][$i] = (int)$engscore;
  $scoreArr["t"][$i] = (int)$totalscore;
}

$okarr = array();

$howmanypasses = $X + $Y + $Z;
$howmanypeople = count($mathscores);
if ($howmanypasses < $N) {
  sqeezeClear($scoreArr["m"], $okarr, $N, $X);
  sqeezeClear($scoreArr["e"], $okarr, $N, $Y);
  sqeezeClear($scoreArr["t"], $okarr, $N, $Z);
} else {
  for ($i = 0; $i < $N; $i++) {
    $okarr[] = $i;
  }
}

asort($okarr);
$lastIndex = count($okarr) - 1;
$cnt = 0;
foreach ($okarr as $no) {
  $no += 1;
  if ($cnt != $lastIndex) {
    $no  .= "\n";
  }
  echo $no;
  $cnt++;
}

/**
 * 合格者を抽出する
 */
function sqeezeClear(&$scoreArr, &$okArr, $total, $thiskamoku)
{
  arsort($scoreArr);
  $cnt = 0;
  foreach ($scoreArr as $no => $score) {
    if (count($okArr) >= $total ||  $cnt == $thiskamoku) {
      break;
    }
    if (in_array($no, $okArr)) {
      continue;
    }
    $okArr[] = $no;
    $cnt++;
  }
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
