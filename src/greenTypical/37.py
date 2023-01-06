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
que=deque()
que.append(1)
while len(que)>0:
  now=que.popleft()
  for nxt in con[now]:
    nxt_time,nxt_route = visited[nxt]
    if nxt_time==_INF:
      visited[nxt][_TIME]=1
      visited[nxt][_ROUTE]=1
      que.append(nxt)
    else:
      now_time,now_route = visited[now]
      if now_time+1==nxt_time:
        visited[nxt][_TIME]=now_time+1
        visited[nxt][_ROUTE]=now_route+1
        que.append(nxt)
      elif now_time+1<nxt_time:
        visited[nxt][_TIME]=now_time+1
        visited[nxt][_ROUTE]=1
        que.append(nxt)

route=visited[n][1]
ans=route%(10**9+7)
print(ans)
