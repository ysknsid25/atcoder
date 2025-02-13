n,k=map(int,input().split())
a = list(map(lambda x: int(x) - 1, input().split()))

dp=[[0 for _ in range(n)] for _ in range(60)]

for i in range(60):
  for j in range(n):
    if i==0:
      dp[i][j]=a[j]
    else:
      dp[i][j]=dp[i-1][dp[i-1][j]]

ans=0
now=0
while k:
  if k&1:
    ans=dp[now][ans]
  now+=1
  k>>=1

print(ans+1)