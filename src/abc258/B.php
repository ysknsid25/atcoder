<?php

fscanf(STDIN, "%d", $N);

$lattice = array();
$max = 0;
for ($i = 1; $i < ($N + 1); $i++) {
  $inputs = str_split(trim(fgets(STDIN)));
  for ($j = 1; $j < ($N + 1); $j++) {
    $index = $j - 1;
    $lattice[$i][$j] = $inputs[$index];
  }
  $tmpmax = max($lattice[$i]);
  if ($tmpmax > $max) {
    $max = $tmpmax;
  }
}

$maxValues = array();
foreach ($lattice as $i => $rows) {
  foreach ($rows as $j => $val) {
    if ($val === $max) {
      $maxValues[$i][$j] = $max;
    }
  }
}

$resultArr = array();
foreach ($maxValues as $initi => $rows) {
  foreach ($rows as $initj => $max) {
    for ($i = -1; $i < 2; $i++) {
      for ($j = -1; $j < 2; $j++) {
        $nexti = $initi;
        $nextj = $initj;
        if ($i == 0 && $j == 0) {
          continue;
        }
        $result = $max;
        for ($cnt = 1; $cnt < $N; $cnt++) {
          $nexti = getNextPosi($nexti, $i, $N);
          $nextj = getNextPosi($nextj, $j, $N);
          $result .= $lattice[$nexti][$nextj];
        }
        $resultArr[] = (int)$result;
      }
    }
  }
}
$ans = max($resultArr);
echo $ans;

function getNextPosi($posi, $move, $max)
{
  $nextposi = abs($posi + $move);
  $nextposi = $nextposi % $max;
  if ($nextposi == 0) {
    return $max;
  }
  return $nextposi;
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
