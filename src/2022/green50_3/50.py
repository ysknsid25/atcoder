from math import ceil
import heapq

n,m,x,y=map(int,input().split())
con=[[] for i in range(n+1)]
for i in range(m):
  a,b,t,k=map(int,input().split())
  con[a].append([b,t,k])
  con[b].append([a,t,k])

que=list()
heapq.heappush(que,[0,x])

times=[10**20 for i in range(n+1)]
times[x]=0
visited=[False for i in range(n+1)]
while len(que)>0:
  now,place=heapq.heappop(que)
  if visited[place]:
    continue
  visited[place]=True
  for to,t,k in con[place]:
    to_time=ceil(now/k)*k+t
    if to_time < times[to]:
      times[to]=to_time
      heapq.heappush(que,[to_time,to])

if times[y]==10**20:
  print(-1)
else:
  print(times[y])