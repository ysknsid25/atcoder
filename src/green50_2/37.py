from collections import deque

def bfs(seen,start,connect):
  que = deque()
  seen[start]=start
  que.append(start)
  while len(que) > 0:
    now = que.popleft()
    rooms=connect[now]
    for to in rooms:
      if seen[to]==0:
        seen[to] = now
        que.append(to)
  return seen

n,m=map(int,input().split())
con=[[] for i in range(n+1)]
for i in range(m):
  a,b=map(int,input().split())
  con[a].append(b)
  con[b].append(a)

seen=[0 for i in range(n+1)]
seen=bfs(seen,1,con)
print("Yes")
for i in range(2,n+1):
  print(seen[i])