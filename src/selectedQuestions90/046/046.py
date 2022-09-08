def makeMap(arr, i, map):
  tmp = arr[i] % 46
  if tmp in map:
    cnt = map[tmp]
    cnt += 1
    map[tmp] = cnt
  else:
    map[tmp] = 1
  return map

n = int(input())

a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))

amap = {}
bmap = {}
cmap = {}
for i in range(0, n):
  amap = makeMap(a, i, amap)
  bmap = makeMap(b, i, bmap)
  cmap = makeMap(c, i, cmap)

ans = 0
for ik, iv in amap.items():
  for jk, jv in bmap.items():
    for lk, lv in cmap.items():
      total = ik + jk + lk
      if total % 46 == 0:
        ans += (iv * jv * lv)

print(ans)