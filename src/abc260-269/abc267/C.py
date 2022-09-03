import numpy as np
n, m = map(int, input().split())
a = list(map(int, input().split()))

maxnum = 0
mlist = np.array([i for i in (1, m) ])
for i in range(0, n):
  if (i+m) > n:
    break
  part = np.array(a[i:(i+m)])
  tmp = 0
  tmp = sum(part * mlist)
  maxnum = max(tmp, maxnum)

print(maxnum)