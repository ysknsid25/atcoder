x, k, d = map(int, input().split())

x = abs(x)
div = x // d
mod = x % d

if div >= k:
  print(x - (d * k))
else:
  remain = k - div
  if remain % 2 == 0:
    print(mod)
  else:
    print(abs(mod - d))