from collections import deque

n,m=map(int,input().split())
con=[[] for i in range(n+1)]
for i in range(m):
  a,b=map(int,input().split())
  con[a].append(b)
  con[b].append(a)

# 0->所要時間, 1->その所要時間で辿り着くルートが何通りあるか
_TIME=0
_ROUTE=1
_INF=10**20
visited=[[_INF,0] for i in range(n+1)]
visited[1][_TIME]=0
visited[1][_ROUTE]=1
que=deque()
que.append(1)
while len(que)>0:
  now=que.popleft()
  for nxt in con[now]:
    now_time,now_route = visited[now]
    nxt_time,nxt_route = visited[nxt]
    if nxt_time==_INF:
      visited[nxt][_TIME]=now_time+1
      visited[nxt][_ROUTE]=now_route
      que.append(nxt)
    else:
      if now_time+1==nxt_time:
        visited[nxt][_ROUTE]+=now_route
    visited[nxt][_ROUTE]%=10**9+7

route=visited[n][1]
if route==_INF:
  print(0)
else:
  print(route)
