<?php
fscanf(STDIN, "%d %d %d", $n, $k, $q);
$initPosi = explode(' ', trim(fgets(STDIN)));
$query = explode(' ', trim(fgets(STDIN)));

$lastRight = $n - 1;

$komaExists = array();
$komaPosi = array();
for ($i = 0; $i < $k; $i++) {
    $posi = $initPosi[$i] - 1;
    $komaExists[$posi] = true;
    $komaPosi[] = $posi;
}

foreach ($query as $target) {
    $targetkoma = $target - 1;
    $posi = $komaPosi[$targetkoma];
    $nextPosi = $posi + 1;
    if ($posi == $lastRight) {
        continue;
    }
    if (empty($komaExists[$nextPosi])) {
        $komaExists[$nextPosi] = false;
    }
    $rightKomaExist = $komaExists[$nextPosi];
    if ($rightKomaExist) {
        continue;
    }
    $komaPosi[$targetkoma] = $nextPosi;
    $komaExists[$posi] = false;
    $komaExists[$nextPosi] = true;
}

$out = "";
foreach ($komaPosi as $posi) {
    $out .= ($posi + 1) . " ";
}
$out = substr($out, 0, -1);
echo $out;
