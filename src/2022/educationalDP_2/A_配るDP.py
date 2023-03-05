n=int(input())
h=list(map(int,input().split()))
h=h + [0,0,0,0,0]
_INF = 10**20
dp = [_INF for i in range(n+5)]
dp[0] = 0
for i in range(0,n+2):
  move1 = dp[i] + abs(h[i]-h[i+1])
  min1 = min(dp[i+1],move1)
  dp[i+1] = min1
  move2 = dp[i] + abs(h[i]-h[i+2])
  min2 = min(dp[i+2],move2)
  dp[i+2] = min2
print(dp[n-1])