n = int(input())
h = list(map(int, input().split()))

INF = 1e18
dp = [INF for i in range(n)]
dp[0] = 0
dp[1] = abs(h[0] - h[1])

for i in range(2, n):
    a = dp[i-1] + abs(h[i] - h[i-1])
    b = dp[i-2] + abs(h[i] - h[i-2])
    dp[i] = min(a, b)

print(dp[n-1])