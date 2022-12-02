def calc_or(l,r,a):
    res = 0
    for i in range(l,r):
        res = res | a[i]
    return res

n=int(input())
a=list(map(int,input().split()))
ans = 10**20

#! Bit全探索
"""
1<<(n+1) = n+1桁の2進数を順にiまで格納する
n=7の場合であれば、0000000~1111111までを探索する
"""
for bit in range(1<<(n+1)):
  #! 右端と左端のどちらかが0になっているものは飛ばす
  if bit&1 == 0 or bit>>n&1 == 0:
    continue

  par = []
  # 右端があるので+1ぶん調べていく
  for i in range(n+1):
    if bit >> i & 1 == 1:
      par.append(i)

  tmp = 0
  for j in range(len(par)-1):
    tmp ^= calc_or(par[j],par[j+1],a)
  ans = min(tmp,ans)

print(ans)