n = int(input())
a = list(map(int, input().split()))

ans = -10 ** 15
minorange = 0
for l in range(n):
  minorange = a[l]
  for r in range(l,n):
    tmpminorange = a[r]
    minorange = min(minorange, tmpminorange)
    res = minorange * (r-l+1)
    ans = max(res, ans)

print(ans)