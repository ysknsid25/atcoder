n = int(input())

dp = [[0 for i in range(3)] for i in range(n + 1)]

hp = []
for i in range(0, n):
  tmp = list(map(int, input().split()))
  hp.append(tmp)

for i in range(0, n):
  for j in range(0,3):
    for k in range(0,3):
      if j == k:
        continue
      else:
        dp[i+1][k] = max(dp[i+1][k], dp[i][j] + hp[i][k])

ans = 0
for i in range(3):
  ans = max(ans, dp[n][i])

print(ans)