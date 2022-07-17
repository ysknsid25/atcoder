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

arsort($scoreArr["m"]);
$cnt = 0;
foreach ($scoreArr["m"] as $no => $score) {
  if (count($okarr) >= $N || $cnt == $X) {
    break;
  }
  $okarr[] = $no;
  unset($scoreArr["e"][$no]);
  unset($scoreArr["t"][$no]);
  $cnt++;
}

arsort($scoreArr["e"]);
$cnt = 0;
foreach ($scoreArr["e"] as $no => $score) {
  if (count($okarr) >= $N || $cnt == $Y) {
    break;
  }
  if (in_array($no, $okarr)) {
    continue;
  }
  $okarr[] = $no;
  unset($scoreArr["t"][$no]);
  $cnt++;
}

arsort($scoreArr["t"]);
$cnt = 0;
foreach ($scoreArr["t"] as $no => $score) {
  if (count($okarr) >= $N ||  $cnt == $Z) {
    break;
  }
  if (in_array($no, $okarr)) {
    continue;
  }
  $okarr[] = $no;
  $cnt++;
}

asort($okarr);
foreach ($okarr as $no) {
  echo ($no + 1) . "\n";
}
