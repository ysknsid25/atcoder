N=int(input())
A=list(map(int,input().split()))
M=int(input())
B=list(map(int,input().split()))
X=int(input())

rice_cake=[False for _ in range(10**5+10)]
for b in B:
    rice_cake[b]=True
    
dp=[False for _ in range(X+1)]
dp[0]=True
for i in range(X):
    if dp[i]:
        for a in A:
            if i+a<=X and not rice_cake[i+a]:
                dp[i+a]=True

if dp[X]:
    print("Yes")
else:
    print("No")