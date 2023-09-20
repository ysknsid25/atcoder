from collections import defaultdict
n,k=map(int,input().split())
c=list(map(int,input().split()))
candy=defaultdict(int)

count=0
for i in range(k):
    if candy[c[i]]==0:
        count+=1
    candy[c[i]]+=1

ans=count
for i in range(k,n):
    out=c[i-k]
    candy[out]-=1
    if candy[out]==0:
        count-=1
    if candy[c[i]]==0:
        count+=1
    ans=max(ans,count)
    candy[c[i]]+=1
print(ans)

