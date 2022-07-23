<?php
fscanf(STDIN, "%d", $n);

$cntArr = array();
for ($i = 0; $i < $n; $i++) {
  $word = str_replace(array("\r\n", "\r", "\n"), "", fgets(STDIN));
  if (empty($cntArr[$word])) {
    $cntArr[$word] = 1;
  } else {
    $cntArr[$word] += 1;
  }
  $samecnt = $cntArr[$word];
  if ($samecnt === 1) {
    echo $word . "\n";
  } else {
    echo $word . "(" . ($samecnt - 1) . ")" . "\n";
  }
}
