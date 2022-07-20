<?php
fscanf(STDIN, "%d", $n);
$ai = array();
$aij = array();
for ($i = 0; $i < $n; $i++) {
  $ai[$i] = $i + 1;
  for ($j = 0; $j <= $i; $j++) {
    if ($j == 0 || $j == $i) {
      $aij[$i][$j] = 1;
    } else {
      $x = 0;
      if (!empty($aij[($i - 1)][($j - 1)])) {
        $x = $aij[($i - 1)][($j - 1)];
      }
      $y = 0;
      if (!empty($aij[($i - 1)][$j])) {
        $y = $aij[($i - 1)][$j];
      }
      $aij[$i][$j] = $x + $y;
    }
  }
  $out = "";
  foreach ($aij[$i] as $j => $val) {
    $out .= $val . " ";
  }
  $out = substr($out, 0, -1);
  echo $out . "\n";
}
