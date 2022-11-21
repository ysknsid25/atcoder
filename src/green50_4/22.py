n,k=map(int,input().split())
pl=list(map(int,input().split()))
totalsum = []
sump = 0
for p in pl:
  exp = (1+p)/2
  sump += exp
  totalsum.append(sump)

ans = 0
for i in range(n-k+1):
  if i==0:
    to = i+k-1
    res = totalsum[to]
  else:
    fr = i-1
    to = i+k-1
    res = totalsum[to]-totalsum[fr]
  ans = max(res,ans)
print(ans)