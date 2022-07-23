<?php
[$a, $b, $c, $d, $e, $f, $x] = explode(' ', trim(fgets(STDIN)));

$tatotal = howlongrun($x, $a, $c);
$aototal = howlongrun($x, $d, $f);

$tadist = $tatotal * $b;
$aodist = $aototal * $e;

if ($tadist > $aodist) {
  echo "Takahashi";
} else if ($tadist < $aodist) {
  echo "Aoki";
} else {
  echo "Draw";
}

function howlongrun($x, $runtime, $resttime)
{
  $cnt = 0;
  $rest = $x;
  $totalruntime = 0;
  while ($rest > 0) {
    if ($cnt % 2 === 0) {
      if (($rest - $runtime) < 0) {
        $totalruntime += $rest;
      } else {
        $totalruntime += $runtime;
      }
      $rest -= $runtime;
    } else {
      $rest -= $resttime;
    }
    $cnt++;
  }
  return $totalruntime;
}
