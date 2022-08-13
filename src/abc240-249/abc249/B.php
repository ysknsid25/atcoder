<?php

$word = str_replace(array("\r\n", "\r", "\n"), "", fgets(STDIN));

if (ctype_upper($word) || ctype_lower($word)) {
  echo "No";
} else {
  $strarr = str_split($word);
  $result = array_count_values($strarr);
  $out = "Yes";
  foreach ($result as $cnt) {
    if ($cnt > 1) {
      $out = "No";
      break;
    }
  }
  echo $out;
}
