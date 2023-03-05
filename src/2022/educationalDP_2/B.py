n,k=map(int,input().split())
h=list(map(int,input().split())) + [0 for i in range(k+1)]
_INF = 10**15
dp = [_INF for i in range(n+k+1)]
dp[0] = 0
for i in range(0,n+k):
  for j in range(1,k+1):
    if i+j > len(h)-1:
      break
    move = dp[i] + abs(h[i]-h[i+j])
    min1 = min(dp[i+j],move)
    dp[i+j] = min1
print(dp[n-1])
