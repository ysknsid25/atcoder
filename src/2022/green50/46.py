H,N=map(int,input().split())
_INF=10**15
dp=[_INF for i in range(H+1)]
dp[0]=0

for i in range(N):
    a,b=map(int,input().split())
    for h in range(H+1):
        if h+a<H:
            dp[h+a]=min(dp[h+a], dp[h]+b)
        else:
            dp[H]=min(dp[H], dp[h]+b)

print(dp[H])