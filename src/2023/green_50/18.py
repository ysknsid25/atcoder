n=int(input())
a=list(map(int,input().split()))
t=sum(a)

ans=0
for i in range(n):
    num=a[i]
    t-=num
    ans+=(t*num)
print(ans%(10**9+7))