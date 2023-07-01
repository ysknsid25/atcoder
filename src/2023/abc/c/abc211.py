s = list("#" + input())
n=len(s)
chokudai=list("#"+"chokudai")

dp=[[0 for i in range(9)] for i in range(n)]

for i in range(n):
    dp[i][0]=1

for i in range(1,n):
    c=s[i]
    for j in range(1,9):
        t=chokudai[j]
        if c==t:
            dp[i][j]=dp[i-1][j]+dp[i][j-1]
        else:
            dp[i][j]=dp[i-1][j]
        dp[i][j]%=10**9+7
print(dp[n-1][8])
