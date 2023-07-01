n,k=map(int,input().split())
c=list(map(str,input().split()))

ans=0
res=0
from collections import deque
from collections import defaultdict
can=defaultdict(int)
q=deque()

for i in range(k):
    can[c[i]]+=1
    q.append(c[i])
    if can[c[i]]==1:
        res+=1
ans=res

for i in range(k,n):
    out = q.popleft()
    q.append(c[i])
    can[out]-=1
    can[c[i]]+=1
    if can[out] ==0:
        res-=1
    if can[c[i]] == 1:
        res+=1
    ans=max(ans,res)
print(ans)

