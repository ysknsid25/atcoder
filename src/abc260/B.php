<?php

fscanf(STDIN, "%d %d %d %d", $N, $X, $Y, $Z);

$mathscores = explode(' ', trim(fgets(STDIN)));
$engscores = explode(' ', trim(fgets(STDIN)));

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
  $scoreArr["m"][$i] = $mathscore;
  $scoreArr["e"][$i] = $engscore;
  $scoreArr["t"][$i] = $totalscore;
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
