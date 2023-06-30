n=int(input())
c=list(map(int,input().split()))
c.sort()
ans=1
mod=10**9+7
for i in range(n):
    if c[i]-i==0:
        print(0)
        exit()
    ans*=(c[i]-i)
    ans%=mod
print(ans)

