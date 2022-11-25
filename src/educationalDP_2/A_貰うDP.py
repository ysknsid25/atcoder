n=int(input())
h=list(map(int,input().split()))
dp = [0 for i in range(n)]
dp[0] = 0
dp[1] = abs(h[1]-h[0])

for i in range(2,n):
  move1 = dp[i-1] + abs(h[i]-h[i-1])
  move2 = dp[i-2] + abs(h[i]-h[i-2])
  cost = min(move1,move2)
  dp[i] = cost

print(dp[n-1])