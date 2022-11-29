n,w=map(int,input().split())
_INF = 10**20*-1
dp = [[_INF for i in range(w+1)] for i in range(n+1)]
dp[0][0] = 0
for i in range(1,n+1):
  iw,iv = map(int,input().split())
  for j in range(0,w+1):
    if j >= iw:
      #! i番目の品物を選ぶ前の時点の重さと価値 + i番目を選んだ時っていうのを舐めていく
      #! 一つ前の品物を選んだ時点でj-iwが0未満の場合はおかしいので選べない
      dp[i][j] = max(dp[i-1][j],dp[i-1][j-iw]+iv)
    dp[i][j] = max(dp[i-1][j],dp[i][j])
ans = 0
for i in range(w+1):
  ans = max(ans, dp[n][i])
print(ans)