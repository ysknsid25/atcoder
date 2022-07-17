<?php
$word = str_replace(array("\r\n", "\r", "\n"), "", fgets(STDIN));

$wordArr = str_split($word);

$charCount = array();
foreach ($wordArr as $char) {
  if (empty($charCount[$char])) {
    $charCount[$char] = 1;
  } else {
    $charCount[$char] += 1;
  }
}

$hasAnswear = false;
foreach ($charCount as $char => $cnt) {
  if ($cnt == 1) {
    echo $char;
    $hasAnswear = true;
    break;
  }
}

if (!$hasAnswear) {
  echo -1;
}
