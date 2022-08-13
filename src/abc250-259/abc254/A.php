<?php

$word = str_replace(array("\r\n", "\r", "\n"), "", fgets(STDIN));
$out = substr($word, (strlen($word) - 2), 2);
echo $out;
