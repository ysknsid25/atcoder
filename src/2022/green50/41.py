s=int(input())
dp = [0 for i in range(2000+1)]
dp[0] = 0
dp[1] = 0
dp[2] = 0
dp[3] = 1
dp[4] = 1
dp[5] = 1
for i in range(6,s+1):
  rsum = sum(dp[3:i-2])+1
  dp[i] = rsum
print(dp[s]%(10**9+7))