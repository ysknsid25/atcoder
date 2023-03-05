n = int(input())
h = [0] + list(map(int, input().split()))
dp = [10**15 for i in range(n + 1)]

dp[1] = 0
dp[2] = abs(h[2] - h[1])

for i in range(3, n+1):
  c1 = dp[i-1] + abs((h[i]-h[i-1]))
  c2 = dp[i-2] + abs((h[i]-h[i-2]))
  c = min(c1,c2)
  dp[i] = c

print(dp[n])