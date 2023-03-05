n=int(input())
a=list(map(int,input().split()))
_INF = 10**20
dp = [_INF for i in range(n)]
dp[0] = 0
dp[1] = abs(a[0]-a[1])
for i in range(2,n):
  p1 = dp[i-1] + abs(a[i]-a[i-1])
  p2 = dp[i-2] + abs(a[i]-a[i-2])
  dp[i] = min(p1,p2)
print(dp[n-1])