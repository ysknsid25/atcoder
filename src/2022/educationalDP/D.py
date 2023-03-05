n, w = map(int, input().split())

weight = []
value = []
for i in range(0, n):
  we, v = map(int, input().split())
  weight.append(we)
  value.append(v)

dp = [[0 for i in range(10 ** 5 + 1)] for i in range(n + 1)]

dp[0][0] = 0

for i in range(0, n):
  for j in range(0, w + 1):
    if j - weight[i] >= 0:
      dp[i + 1][j] = max(dp[i+1][j], dp[i][j - weight[i]] + value[i])

    dp[i + 1][j] = max(dp[i+1][j], dp[i][j])
    
print(dp[n][w])