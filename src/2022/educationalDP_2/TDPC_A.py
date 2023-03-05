n=int(input())
p=[0] + list(map(int, input().split()))
maxsc = sum(p)
_INF = 10**20*-1
dp = [[_INF for i in range(maxsc+1)] for i in range(n+1)]
dp[0][0] = 0
for i in range(1,n+1):
  sc = p[i]
  for j in range(maxsc+1):
    sc1 = dp[i-1][j]
    if sc1 >= 0:
      dp[i][j] = sc1
    if j-sc >= 0: 
      sc2 = dp[i-1][j-sc]+sc
      if sc2 >= 0:
        dp[i][j] = sc2

ans = 0
for i in range(maxsc+1):
  sc = dp[n][i]
  if sc >= 0:
    ans += 1
print(ans)