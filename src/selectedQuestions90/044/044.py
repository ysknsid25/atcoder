def getIndex(i, s, n):
  return (i-s-1)%n

n, q = map(int, input().split())
a = list(map(int, input().split()))

s = 0
for i in range(q):
  t, x, y = map(int, input().split())
  rx = getIndex(x, s, n)
  ry = getIndex(y, s, n)
  if t == 1:
    tmpx = a[rx]
    tmpy = a[ry]
    a[rx] = tmpy
    a[ry] = tmpx
  elif t == 2:
    s += 1
  else:
    print(a[rx])

