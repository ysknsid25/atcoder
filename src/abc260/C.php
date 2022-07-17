<?php

fscanf(STDIN, "%d %d %d", $N, $X, $Y);

$Rarr = array();
$Barr = array();

for ($i = 1; $i < 11; $i++) {
  $Rarr[$i] = 0;
  $Barr[$i] = 0;
}

$Rarr[$N] = 1;

while (true) {
  $doRExchange = true;
  foreach ($Rarr as $lv => $cnt) {
    if ($cnt == 0) {
      continue;
    }
    if ($lv > 1) {
      $doRExchange = $doRExchange && ($cnt > 0);
      $nextlv = $lv - 1;
      for ($i = 0; $i < $cnt; $i++) {
        $Rarr[$lv] -= 1;
        $Rarr[$nextlv] += 1;
        $Barr[$lv] += $X;
      }
    }
  }
  $doBExchange = true;
  foreach ($Barr as $lv => $cnt) {
    if ($cnt == 0) {
      continue;
    }
    if ($lv > 1) {
      $doBExchange = $doBExchange && ($cnt > 0);
      $nextlv = $lv - 1;
      for ($i = 0; $i < $cnt; $i++) {
        $Barr[$lv] -= 1;
        $Rarr[$nextlv] += 1;
        $Barr[$nextlv] += $Y;
      }
    }
  }
  if (!$doRExchange && !$doBExchange) {
    break;
  }
  var_dump($Rarr);
  var_dump($Barr);
  break;
}
echo $Barr[1];
