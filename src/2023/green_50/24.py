n,m,x=map(int,input().split())
a=[[] for i in range(n)]
c=[]
for i in range(n):
  tmp=list(map(int,input().split()))
  for j in range(m+1):
    if j==0:
      c.append(tmp[0])
    else:
      a[i].append(tmp[j])

p=2**n

ans=10**15
for bit in range(p):
  price=0
  skill=[0 for i in range(m)]
  for i in range(n):
    if (bit >> i) & 1:
      price+=c[i]
      for j in range(m):
        skill[j]+=a[i][j]
  
  isAchive=True
  for s in skill:
    if s < x:
      isAchive=False
      break

  if isAchive:
    ans=min(ans,price)

if ans == 10**15:
  print(-1)
else:
  print(ans)
