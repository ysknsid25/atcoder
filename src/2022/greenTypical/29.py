from collections import deque

n,m=map(int,input().split())
con=[[] for i in range(n+1)]
for i in range(m):
  a,b=map(int,input().split())
  con[a].append(b)

def bfscity(n,s,con):
  visited=[False for i in range(n+1)]
  cnt=0
  que=deque()
  que.append(s)
  while len(que)>0:
    now=que.popleft()
    if visited[now]:
      continue
    visited[now]=True
    cnt+=1
    for nxt in con[now]:
      que.append(nxt)
  return cnt

ans=0
for s in range(1,n+1):
  ans+=bfscity(n,s,con)
print(ans)