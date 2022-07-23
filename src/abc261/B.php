<?php

fscanf(STDIN, "%d", $n);

$resultArr = array();
for ($i = 0; $i < $n; $i++) {
  $word = str_replace(array("\r\n", "\r", "\n"), "", fgets(STDIN));
  $resultArr[] = str_split($word);
}

$out = "correct";
for ($i = 0; $i < $n; $i++) {
  for ($j = 0; $j < $n; $j++) {
    $resulta = $resultArr[$i][$j];
    $resultb = $resultArr[$j][$i];
    if ($i === $j) {
      if ($resulta !== "-") {
        $out = "incorrect";
        break 2;
      }
    } else {
      $reverseResult = getReverseResult($resultb);
      if ($resulta !== $reverseResult) {
        $out = "incorrect";
        break 2;
      }
    }
  }
}

echo $out;

function getReverseResult($result)
{
  if ($result === "D") {
    return "D";
  }
  if ($result === "W") {
    return "L";
  }
  return "W";
}
