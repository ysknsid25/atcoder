n,w = map(int,input().split())
_INF = -10**15
dp = [[_INF for i in range(10**5+1)] for i in range(n+1)]
dp[0][0] = 0

for i in range(1,n+1):
  iw,iv = map(int,input().split())
  for j in range(w+1):
    if j-iw >= 0:
      #! 選べる
      dp[i][j] = max(dp[i-1][j], dp[i-1][j-iw]+iv)
    else:
      #! 選べない場合
      dp[i][j] = dp[i-1][j]

ans = _INF
for i in range(1,w+1):
  ans = max(ans, dp[n][i])
print(ans)