s=int(input())
dp=[0 for i in range(s+1)]
for i in range(3,s+1):
  dp[i]=1

total=0
for i in range(6,s+1):
  total+=dp[i-3]
  dp[i]=total+1
ans=dp[s]%(10**9+7)
print(ans)