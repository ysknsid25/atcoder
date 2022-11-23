n=int(input())
num = set()
for a in range(2,10**5+1):
  for b in range(2,35):
    if a**b <= n:
      num.add(a**b)
    else:
      break
ans = n-len(num)
print(ans)