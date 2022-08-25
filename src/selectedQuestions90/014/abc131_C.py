n = int(input())
amap = {}
bmap = {}
for i in range(0, n):
  a, b = map(int, input().split())
  amap[i] = a
  bmap[i] = b

sortedb = sorted(bmap.items(), key=lambda x:x[1])

now = 0

isEnd = True
for keyval in sortedb:
  key = keyval[0]
  time = keyval[1]
  interval = amap[key]
  now += interval
  if now > time:
    isEnd = False
    break

if isEnd:
  print("Yes")
else:
  print("No")
