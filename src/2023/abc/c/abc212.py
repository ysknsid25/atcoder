n,m=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
a.sort()
b.sort()
ans=10**18
i=0
j=0
while i<n and j<m:
    ans=min(ans,abs(a[i]-b[j]))
    if a[i]<b[j]:
        i+=1
    elif a[i]>b[j]:
        j+=1
    else:
        print(0)
        exit()
print(ans)