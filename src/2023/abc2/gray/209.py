n=int(input())
c=list(map(int,input().split()))
c.sort()
ans=c[0]
for i in range(1,n):
    ans*=c[i]-i
    ans%=(10**9+7)
    if ans==0:
        print(0)
        exit()
print(ans)