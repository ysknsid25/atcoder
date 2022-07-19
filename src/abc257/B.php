<?php
fscanf(STDIN, "%d %d $d", $n, $k, $q);
$initPosi = explode(' ', trim(fgets(STDIN)));
$query = explode(' ', trim(fgets(STDIN)));

$komaExists = array();
$komaPosi = array();
for ($i = 0; $i < $n; $i++) {
    $posi = $initPosi[$i] - 1;
    $komaExists[$posi] = true;
    $komaPosi[] = $posi;
}

$lastRight = $n - 1;
foreach ($query as $target) {
    $targetkoma = $target - 1;
    $posi = $komaPosi[$targetkoma];
    $nextPosi = $posi + 1;
    if ($posi == $lastRight) {
        continue;
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
    $out = ($posi + 1) . " ";
}
echo substr($out, -1);
