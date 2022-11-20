n=int(input())
a = 10**5+1
b = 30
ex = set()
for i in range(2,a):
  for j in range(2,b+1):
    res = i**j
    if res > n:
      break
    else:
      ex.add(res)

ans = n-len(ex)