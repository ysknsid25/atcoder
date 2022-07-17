<?php

fscanf(STDIN, "%d", $k);
$ninehour = date("H:i", strtotime('+' . $k . ' minute', strtotime("21:00")));
echo $ninehour;
