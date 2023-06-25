n,m=map(int,input().split())
con=[[] for i in range(n+1)]

for i in range(m):
    a,b=map(int,input().split())
    con[a].append(b)

from collections import deque
ans=0
for i in range(1,n+1):
    start=i
    q=deque()
    q.appendleft(start)
    visited=[False for i in range(n+1)]
    visited[start]=True
    while len(q)>0:
        now=q.popleft()
        ans+=1
        for to in con[now]:
            if not visited[to]:
                visited[to]=True
                q.appendleft(to)
print(ans)