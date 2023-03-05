n,w=map(int,input().split())
_MAX_N = n+10
_MAX_V = 10**5 + 10
_INF = 10**20
dp = [[_INF for i in range(_MAX_V) ] for i in range(_MAX_N)]
dp[0][0] = 0

for i in range(n):
  iw, iv = map(int, input().split())
  idx = i+1
  for j in range(0,_MAX_V):
    if j - iv >= 0:
      dp[idx][j] = min(dp[idx][j], dp[idx-1][j-iv]+iw)
    dp[idx][j] = min(dp[idx][j], dp[idx-1][j])

ans = 0
for v in range(0,_MAX_V):
  if dp[n][v] <= w:
    ans = v
print(ans)