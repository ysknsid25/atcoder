"""
三分探索
・とある時点までは減少し、最小値を迎えたあとは増加する場合
・とある時点までは増加し、最大値を迎えたあとは減少する場合
この二つのパターンにおいて効果を発揮する。

三分探索の基本的な形はどれも同じ
"""

import math
def speed(a,b,x):
  g = x+1
  res = b*x+a/math.sqrt(g)
  return res

a,b=map(int,input().split())
ans = -1
l=0
r=10**18
while l+3 <= r:
  c1 = (l*2+r)//3
  c2 = (l+r*2)//3
  if speed(a,b,c1) >= speed(a,b,c2):
    l = c1
  else:
    r = c2

ans = min(speed(a,b,l),speed(a,b,l+1),speed(a,b,r))
print(ans)