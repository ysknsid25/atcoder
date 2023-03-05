x,k,d = map(int, input().split())
ans = 0
x = abs(x)
border = x-(k*d)
if border >= 0:
  ans = abs(border)
  print(ans)
else:
  m = x//d
  l = x - (d*m)
  r = k-m
  if r%2==1:
    ans = abs(l-d)
  else:
    ans = abs(l)
  print(ans)