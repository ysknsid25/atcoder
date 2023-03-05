n = int(input())
a = list(map(int, input().split()))

minorange = 0
ans = 0
for l in range(n):
  minorange = a[l]
  for r in range(l,n):
    minorange = min(minorange, a[r])
    ans = max(ans, minorange * (r - l +1))

print(ans)