import math
a,b=map(int,input().split())
ans = 10**20
notupd = 0
g = 0
while notupd < 3:
  time = (b*g) + (a/math.sqrt(g+1))
  if time < ans:
    ans = time
  else:
    notupd += 1
  g+=1
print(ans)