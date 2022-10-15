n = int(input())
a = list(map(int, input().split()))

a.sort()
aset = set(a)
amap = {}

for i in range(n):
  val = i + 1
  key = aset[i]
  amap[key] = val

for i in range(n):
  key = a[i]
  val = amap[key]
  ans = n - val
  print(ans)