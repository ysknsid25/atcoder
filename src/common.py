# 文字列を受け取る場合
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
