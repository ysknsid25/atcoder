<?php
[$La, $Ra, $Lb, $Rb] = explode(' ', trim(fgets(STDIN)));

$cnt = 0;
for ($i = 0; $i <= 100; $i++) {
  if ($La <= $i && $i <= $Ra && $Lb <= $i && $i <= $Rb) {
    $cnt++;
  }
}

if ($cnt !== 0) {
  $cnt -= 1;
}
echo $cnt;
