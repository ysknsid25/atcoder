# 重要例題 二分探索法
# Pythonではbisectを使う
import bisect
n = int(input())
a = list(map(int, input().split()))
q = int(input())

a.sort()

for i in range(0, q):
  b = int(input()) 
  tmp1 = int(1e9)
  tmp2 = int(1e9)
  num = bisect.bisect_left(a, b)
  if num >= 1:
    tmp1 = abs(a[num-1] - b)
  if num <= n-1:
    tmp2 = abs(a[num] - b)
  ans = min(tmp1, tmp2)
  print(ans)
