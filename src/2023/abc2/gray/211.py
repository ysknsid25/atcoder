n,m=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
a.sort()
b.sort()

ans=10**18
l=0
r=0
while l<n and r<m:
    ans=min(ans,abs(a[l]-b[r]))
    if a[l]<b[r]:
        l+=1
    else:
        r+=1
print(ans)