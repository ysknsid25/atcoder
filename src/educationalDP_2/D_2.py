n, w = map(int, input().split())
_INF = -10**20
dp = [[_INF for i in range(w+10)] for i in range(n+10)]
dp[0][0] = 0

for i in range(1, n+1):
    iw, iv = map(int, input().split())
    for j in range(0, w+10):
        if j - iw >= 0:
            #! 選べるときは、選べない場合と比べてどちらが大きくなるかを決める
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-iw] + iv)
        else:
            #! 選べない場合はひとつ前の品物を選ぶか選ばないかの時点の値に決まる
            dp[i][j] = dp[i-1][j]

ans = 0
for i in range(w+1):
    ans = max(ans, dp[n][i])
print(ans)
