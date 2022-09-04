
n, m = map(int, input().split())
a = list(map(int, input().split()))

INF = 1e18 * -1

dp = [[INF for i in range(n+1)] for i in range(m+1)]
dp[0][0] = 0

maxnum = 0 
for i in range(0, n+1):
  for j in range(0, m+1):
    dp[i+1][j] = max(dp[i+1][j], dp[i][j])
    if j > 0:
      dp[i+1][j] = max(dp[i+1][j], dp[i][j-1] + a[i] * j)

print(maxnum)