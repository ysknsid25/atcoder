h,n=map(int,input().split())
_INF=10**10
dp=[_INF for i in range(h+1)]
dp[0]=0
for i in range(n):
  a,b=map(int,input().split())
  for i in range(h+1):
    if i+a<=h:
      dp[i+a]=min(dp[i+a],dp[i]+b)
    else:
      dp[h]=min(dp[h],dp[i]+b)
print(dp[h])