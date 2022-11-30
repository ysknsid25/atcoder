n, w = map(int, input().split())
_INF = 10**20
_MAX_VAL = 10**5+10
dp = [[_INF for i in range(_MAX_VAL)] for i in range(n+10)]
dp[0][0] = 0
for i in range(1, n+1):
    iw, iv = map(int, input().split())
    for j in range(_MAX_VAL):
        if j-iv >= 0:
            #! 選べる時
            dp[i][j] = min(dp[i][j], dp[i-1][j-iv] + iw)
        #! 選べないときは毎回
        dp[i][j] = min(dp[i][j], dp[i-1][j])

ans = 0
for v in range(_MAX_VAL):
    if dp[n][v] <= w:
        ans = v
print(ans)
