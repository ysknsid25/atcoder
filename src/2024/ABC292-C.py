n=int(input())
num = [0 for _ in range(0,n+1)]
for x in range(1, n+1):
  for y in range(1, n+1):
    if x*y <= n:
      num[x*y] += 1
    else:
      break

ans = 0
for i in range(1, n+1):
  ab = num[i]
  cd = num[n-ab]
  ans += ab*cd

print(ans)