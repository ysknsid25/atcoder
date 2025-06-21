"""
単語数の数え上げ
説明
文章中に出現する単語のうち、大文字のアルファベットまたは数字から始まる単語が何種類あるか数える関数solutionを作成してください。
関数は文章を受け取る引数を1つ持ちます。大文字のアルファベットまたは数字(0~9)から始まる単語の種類数を整数で返してください。

仕様
作成する関数solutionは1つの引数textを持ちます。textには単語が分かち書きされた英語の文章が与えられます。
文末等につくピリオドやカンマと直前の単語の間に半角スペースは含まれません。
文字列中には半角英数字、ピリオド、カンマ、ダブルクォーテーション、半角スペースと下に示す記号類が含まれます。単語はピリオドとカンマ、ダブルクォーテーション、半角スペースで区切られる1文字以上の文字列です。下に示された記号類は単語の区切り文字ではありません。

-
=
'
$
%
大文字小文字の違いを無視すると一致する単語は、別の単語と見なしてください。たとえば、"Text"と"TEXT"は2種類の単語と数えてください。

例
例1
入力: "M3 is a company which provides medical-related services through the use of the Internet since 2000. M3 stands for Medicine, Media and Metamorphosis."
出力: 6
説明: 入力に、大文字で始まる単語は6つ5種類 (M3, Internet, M3, Medicine, Media, Metamorphosis)、数字で始まるのは1つ1種類(2000)含まれます。これらの種類の数の合計6を出力します。
制約
textの長さ
n
について、
0
≤
n
≤
1
0
5
を満たす。
"""

import re


def solution(text):
    words = re.findall(r'\b[A-Z0-9][\w\'\-\=\$\%]*', text)
    unique_words = set(words)
    return len(unique_words)




