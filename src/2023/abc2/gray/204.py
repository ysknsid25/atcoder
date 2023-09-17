from collections import defaultdict
n=int(input())
a=list(map(int,input().split()))
b=defaultdict(int)
for i in range(n):
    b[a[i]]+=1
a.sort()
aset=set(a)
ans=0
for num in aset:
    ans+=b[num]*(n-b[num])
    n-=b[num]
print(ans)