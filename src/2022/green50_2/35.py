def price(n,a,b):
  strn = str(n)
  d = len(strn)
  p = a*n + b*d
  return p

a,b,x = map(int, input().split())

if x<price(1,a,b):
  print(0)
  exit()

left = 1
right = 10 ** 10
ans = 0
while 1 < right - left:
  mid = (left + right)//2
  if price(mid,a,b) <= x:
    left = mid
  else:
    right = mid
  ans = left

if 10**9 < ans:
  ans = 10**9
print(ans)