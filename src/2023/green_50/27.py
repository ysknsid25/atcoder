from collections import deque
n,m=map(int,input().split())
r=[[] for i in range(n+1)]

for i in range(m):
    a,b=map(int,input().split())
    r[a].append(b)
    tmp=set(r[a])
    r[a]=list(tmp)
    
ans=0
for i in range(1,n+1):
    visited=[False for i in range(n+1)]
    que=deque()
    ans+=1
    que.append(i)
    visited[i]=True
    while len(que) > 0:
        fr=que.popleft()
        for to in r[fr]:
            if not visited[to]:
                visited[to]=True
                ans+=1
                que.append(to)
print(ans)