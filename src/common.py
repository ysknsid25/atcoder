# 文字列を受け取る場合
import math
from this import d


S = input()

# 整数を受け取る場合
N = int(input())

# 小数を受け取る場合
F = float(input())

# 文字列を受け取る場合
A, B = input().split()

# 整数を受け取る場合
X, Y, Z = map(int, input().split())

# 小数を受け取る場合
H, M, S = map(float, input().split())

# 文字列を受け取る場合
A = input().split()

# 整数列を受け取る場合
A = list(map(int, input().split()))

# 小数列を受け取る場合
A = list(map(float, input().split()))

# 複数行の文字列を受け取る場合
A = [input().split() for _ in range(N)]

# 複数行の整数列を受け取る場合
A = [list(map(int, input().split())) for _ in range(N)]

# 複数行の小数列を受け取る場合
A = [list(map(float, input().split())) for _ in range(N)]

# 配列の初期化
mul_tbl = [[x * y for x in range(1, 4)] for y in range(1, 5)]  # 1~3, 1~4

# 整数配列の生成
b = list(range(m+1))

# 文字列を配列に変換
list(test_str)

# 配列の長さ
len(arr)

# マップにすでにキーがあるかどうかを確認する
'key' in d

# マップにすでに値があるかどうかを確認する
'val' in d.values()

# [s[i], t[i]]の配列の要素を順にSに取り出してループさせる
for S in [s[i], t[i]]:
    print(S)

# 配列の要素の追加
arr.append('youso')

# 指定した位置の配列の要素を削除し、値を取得する
arr.pop(index)

# 指定した値が配列のどのインデックスにあるかを検索
# 配列に含まれているか？を調べてからでないと、.indexはエラーを吐く
result = 0 in mylist
idx = mylist.index(3)  # mylistに含まれる整数値3の最小のインデックスを求める
print(idx)  # 5

# 文字列型への変換
str(notexistx)

# 辞書をループで回す
for k in d:
    print(k)

for v in d.values():
    print(v)

for k, v in d.items():
    print(k, v)

# 平方根の計算
math.sqrt(x)

# 辞書の初期化
map = {"app": 1, "pen": 2}

# 配列の要素に含まれる値の個数をカウントする
arr.count('search')

# 文字列のtrim
str = "hogehoge"
result = str[0:1]  # h
result = str[:1]  # h
result = str[-1:]  # e

# 配列 ソート
arr.sort()

# 配列 降順ソート
arr.sort(reverse=True)

# ソートし新たなリストを作成
new_list = sorted(org_list)

# 配列から文字列を生成
A = ["a", "b", "c"]
StrA = "".join(A)
print(StrA)

# mapをキーで昇順ソート
dic = {"X": 80, "A": 200, "E": 5, "R": 20, "S": 40}
dic2 = sorted(dic.items())

# mapをキーで降順ソート
dic2 = sorted(dic.items(), reverse=True)
print(dic2)

# mapをvalueで昇順ソート
dic2 = sorted(dic.items(), key=lambda x: x[1])
print(dic2)

# mapをvalueで降順ソート
dic2 = sorted(dic.items(), key=lambda x: x[1], reverse=True)
print(dic2)

# 進数変換
def Base_10_to_n(n, b):
    if n // b:
        return Base_10_to_n(n // b, b) + str(n % b)
    return str(n % b)

# 素因数分解
def pf(n):
  num = int(pow(n, 0.5))
  rem = n
  p = []
  for i in range(2, num+1):
    while(rem % i == 0):
      rem = rem // i
      p.append(i)
  else:
    if rem != 1:
      p.append(rem)
  return p