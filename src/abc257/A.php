<?php
fscanf(STDIN, "%d %d", $N, $X);

$alphaArr = array(
    "A", "B", "C", "D", "E",
    "F", "G", "H", "I", "J",
    "K", "L", "M", "N", "O",
    "P", "Q", "R", "S", "T",
    "U", "V", "W", "X", "Y",
    "Z"
);

$str = "";
foreach ($alphaArr as $alpha) {
    for ($i = 0; $i < $N; $i++) {
        $str .= $alpha;
    }
}

echo substr($str, ($X - 1), 1);
