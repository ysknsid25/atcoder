import math

x, y, n = map(int, input().split())

div = math.ceil(y/3)

if x > div:
  ynum = n // 3
  yc = y * ynum
  xc = x * (n%3)
  sum = xc + yc
  print(sum)
else:
  sum = x * n
  print(sum)