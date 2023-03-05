def price(n,a,b):
  strn = str(n)
  ln = len(strn)
  p = a*n + b*ln
  return p

a,b,x = map(int, input().split())

if x < price(1,a,b):
  print(0)
  exit()

l=1
r=10**9+1
while r-l > 1:
  mid = (l+r)//2
  midp = price(mid,a,b)
  if midp <= x:
    l = mid
  else:
    r = mid

if l > 10**9:
  l = 10**9

print(l)
