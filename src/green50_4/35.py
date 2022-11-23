def price(n,a,b):
  strn = str(n)
  length = len(strn)
  p = a*n + b*length
  return p

a,b,x = map(int,input().split())
if x < price(1,a,b):
  print(0)
  exit()

l=1
r=10**15
while r-l > 1:
  mid = (l+r)//2
  midn = price(mid,a,b)
  if x < midn:
    r=mid
  else:
    l=mid

if l > 10**9:
  l = 10**9

print(l)