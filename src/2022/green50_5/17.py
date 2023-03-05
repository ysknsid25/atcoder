n=int(input())
res = set()
for a in range(2,10**5+1):
    for b in range(2,35):
      if a**b <= n:
        res.add(a**b)
      else:
        break
ans = n-len(res)
print(ans)