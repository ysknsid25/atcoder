h,n=map(int,input().split())
_INF=10**20
dp=[_INF for i in range(h+1)]
dp[0]=0
for i in range(n):
  a,b=map(int,input().split())
  for j in range(0,h+1):
    d=j+a
    if d>h:
      d=h
    dp[d]=min(dp[d],dp[j]+b)
print(dp[h])
    