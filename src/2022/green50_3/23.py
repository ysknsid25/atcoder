n = int(input())
a = list(map(int, input().split()))
maxcnt = -10**15
for l in range(0,n):
  amin = a[l]  
  for r in range(l, n):
    amin = min(amin, a[r])
    cnt = amin*(r-l+1)
    maxcnt = max(maxcnt, cnt)
print(maxcnt)