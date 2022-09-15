def pf(n):
  num = int(pow(n, 0.5))
  rem = n
  p = []
  for i in range(2, num+1):
    while(rem % i == 0):
      rem = rem // i
      p.append(i)
  else:
    if rem != 1:
      p.append(rem)
  return p

n = int(input())
p = pf(n)

cnt = len(p)
ans = 0
tmp = 1
while tmp < cnt:
    tmp *= 2
    ans += 1

print(ans) 
