n=int(input())
a=list(map(int,input().split()))
ans = 0
for l in range(0,n):
  minorange = 10**5+1
  for r in range(l,n):
    minorange = min(minorange, a[r])
    length = r-l+1
    eat = minorange*length
    ans = max(ans, eat)
print(ans)