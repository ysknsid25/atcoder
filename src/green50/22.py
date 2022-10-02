"""
和の公式
https://rikeilabo.com/sum-formula-of-numerical-sequence

期待値の線形性
『問題解決のための「アルゴリズム×数学」が基礎からしっかり身につく本』
P.181

サイコロがp面の場合の期待値は、期待値の線形性と組み合わせることで、
1/2 * p * (1+p) * (1/p) = (1+p)/2
となる。

後は区間和を予め計算しておく。
区間和=n番目までの和
"""

n, k = map(int, input().split())
p = list(map(int, input().split()))
rangesum = []

for i in range(n):
  me = p[i]
  sump = (1 + me) / 2
  if i == 0:
    rangesum.append(sump)
  else:
    tmp = sump + rangesum[i-1]
    rangesum.append(tmp)

ans = -10 ** 15
for i in range(n-k+1):
  if i == 0:
    res = rangesum[i+k-1]
  else:
    res = rangesum[i+k-1] - rangesum[i-1]
  ans = max(ans, res)

print(ans)


