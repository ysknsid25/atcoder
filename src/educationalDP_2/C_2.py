n=int(input())
N=n+10
dp = [[0,0,0] for i in range(N)]

for i in range(1,n+1):
  hp = list(map(int, input().split()))
  if i==1:
    dp[i][0],dp[i][1],dp[i][2] = hp[0],hp[1],hp[2]
  else:
    for t in range(3):
      for y in range(3):
        if t==y:
          continue
        dp[i][t] = max(dp[i][t], dp[i-1][y]+hp[t])

print(max(dp[n][0],dp[n][1],dp[n][2]))