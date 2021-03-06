<?php

//数字の入力
fscanf(STDIN, "%d", $orange);
[$N, $X, $Y, $Z] = explode(' ', trim($inputs[0]));
[$N, $X, $Y, $Z] = explode(' ', trim(fgets(STDIN)));

//文字列の入力
$word = str_replace(array("\r\n", "\r", "\n"), "", fgets(STDIN));

//複数の整数入力
$inputs = explode(' ', trim(fgets(STDIN)));
[$n, $k] = explode(' ', trim(fgets(STDIN)));

//後ろから一文字を削除
$rest = substr($str, 0, -1);

//指数計算
$ret = pow(2, 8); //256

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

//日時の取得
//https://qiita.com/shuntaro_tamura/items/b7908e6db527e1543837
$datetime = date("h:i", strtotime('+100 minute', strtotime("21:00")));

//配列の最大値
$maxvalue = max($array);

//配列内の値を検索。マッチした最初のキーを返す
//見つからない場合はfalseを返す
$result = array_search('PHP', $array);

//配列内の値を検索。マッチした全てのキーを返す
$result = array_keys($array, "PHP");

//中央値を返す
function median($list)
{
  sort($list);
  if (count($list) % 2 == 0) {
    return (($list[(count($list) / 2) - 1] + $list[((count($list) / 2))]) / 2);
  } else {
    return ($list[floor(count($list) / 2)]);
  }
}

$aphaArr = [
  "a", "b", "c", "d", "e",
  "f", "g", "h", "i", "j",
  "k", "l", "m", "n", "o",
  "p", "q", "r", "s", "t",
  "u", "v", "w", "x", "y",
  "z"
];

//四捨五入
round(3.1415, 2);
//→　3.14
round(271828, -2);
//→　271800

//切り上げ
ceil(3.14);
//→　4

//切り捨て
floor(3.14);
//→　3

//文字列が全て大文字か
ctype_upper($text);

//文字列が全て小文字か
ctype_lower($text);

//配列内の同じ値をカウントする
$result = array_count_values($arr);

//配列を指定のサイズ、初期値で初期化する
$a = array_fill(0, 3, '-');
// $a == array('-', '-', '-')

//2次元配列を初期化するにはこれ
$a = array_fill(0, 3, array_fill(0, 2, 1));
