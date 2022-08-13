<?php
$word = str_replace(array("\r\n", "\r", "\n"), "", fgets(STDIN));
$len = strlen($word);
$repeat = 6 / $len;

$out = "";
for ($i = 0; $i < $repeat; $i++) {
  $out .= $word;
}
echo $out;
