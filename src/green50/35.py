# 重要例題 二分探索

def price(a, b, n):
  strn = str(n)
  d = len(strn)
  p = a * n + b * d
  return p

a, b, x = map(int, input().split())

left = 1
right = 10 ** 10

if x < price(a,b,1):
  print(0)
  exit()

ans = 0
while 1 < right - left:
  n = (left + right) // 2
  p = price(a,b,n) 
  if p <= x:
    left = n
  else:
    right = n
  ans = left

if ans > 10 ** 9:
  print(10 ** 9)
else:
  print(ans)