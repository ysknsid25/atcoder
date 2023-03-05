s=list(input())
ss=["c","h","o","k","u","d","a","i"]
n=len(s)
dp=[[0 for i in range(9)] for i in range(n+1)]
dp[0][0]=1
for i in range(n+1):
  for k in range(9):
    if i==0 and k==0:
      dp[0][0]=1
      continue
    elif i==0 and k>0:
      dp[i][k]=0
      continue
    elif i>0 and k==0:
      dp[i][k]=1
      continue
    a=s[i-1]
    b=ss[k-1]
    if a==b:
      dp[i][k]=dp[i-1][k]+dp[i][k-1]
    else:
      dp[i][k]=dp[i-1][k]
  dp[i][k]%=10**9+7
print(dp[n][8])
