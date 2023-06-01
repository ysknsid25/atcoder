n,k,a=map(int,input().split())
ans=a
while k>1:
    k-=1
    ans+=1
    if ans>n:
        ans=1
print(ans)