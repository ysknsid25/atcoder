n,k,x=map(int,input().split())
a=list(map(int,input().split()))
for i in range(n):
    d=a[i]//x #使えるチケットの枚数
    if d<=k:
        a[i]=a[i]%x
        k-=d
    else:
        a[i]=a[i]-k*x
        k=0
a.sort(reverse=True)
ans=0
for i in range(n):
    if k>0:
        k-=1
        continue
    ans+=a[i]
print(ans)