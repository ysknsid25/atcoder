n, x = map(int, input().split())
ab = [list(map(int, input().split())) for _ in range(n)]
# i回目のジャンプで座標xにいれるかどうか？が分かればイイ
dp = [[False for _ in range(x + 1)] for _ in range(n+1)]
dp[0][0] = True
for i in range(n):
  a, b = ab[i]
  for x in range(1, x+1):
    if x-a >= 0 and dp[i][x-a]:
      dp[i+1][x] = True
    if x-b >= 0 and dp[i][x-b]:
      dp[i+1][x] = True

if dp[n][x]:
  print('Yes')
else:
  print('No')