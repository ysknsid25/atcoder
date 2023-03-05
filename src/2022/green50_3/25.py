n = int(input())
h = list(map(int, input().split()))
dp = [-1 for i in range(n)]

dp[0] = 0
dp[1] = abs(h[1]-h[0])
for i in range(2,n):
  h1 = abs((h[i] - h[i-1])) + dp[i-1]
  h2 = abs((h[i] - h[i-2])) + dp[i-2]
  minh = min(h1, h2)
  dp[i] = minh

print(dp[n-1])