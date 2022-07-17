<?php

//数字の入力
fscanf(STDIN, "%d", $orange);

//文字列の入力
$word = str_replace(array("\r\n", "\r", "\n"), "", fgets(STDIN));

//複数の整数入力
$inputs = explode(' ', trim(fgets(STDIN)));

//文字列を配列に分割する
$strarr = str_split($word);

//キーを保持したまま昇順ソート
asort($inputs);

//キーを保持したまま降順ソート
arsort($inputs);

//tanの角度(ラジアン=2πr=360°)を求める
$beforerad = atan2($b, $a);

//ラジアンを普通の角度に戻す
$beforedeg = rad2deg($beforerad);

//普通の角度をラジアンに変換する
$afterRad = deg2rad($afterDeg);

//平方根
$r = sqrt(($a * $a + $b * $b));

//ラジアンからcos(x座標), sin(y座標)を導出する
$x = cos($afterRad);
$y = sin($afterRad);
