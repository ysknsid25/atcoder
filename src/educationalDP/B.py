n, k = map(int, input().split())
h = list(map(int, input().split()))

INF = 1e9
dp = [INF for i in range(n)]
dp[0] = 0
dp[1] = abs(h[0] - h[1])

for i in range(2, n):
    res = 1e9
    for j in range(0,k):
        a = dp[i-(j+1)] + abs(h[i] - h[i-(j+1)])
        res = min(res, a)
    dp[i] = res

print(dp[n-1])