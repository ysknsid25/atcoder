from math import ceil
#! ダイクストラ法
"""
行った場所には印をつける。
その場所から行ける場所を調べていき、その場所から行った場合の時間と
行ける場所に登録されている時間(別の場所からの所要時間)を比較し、
より早く到着できる方の時間を登録する。
"""

n,m,x,y=map(int,input().split())
con=[[] for i in range(n+1)]
for i in range(m):
  a,b,t,k=map(int,input().split())
  con[a].append([b,t,k])
  con[b].append([a,t,k])

que=list()
import heapq
heapq.heappush(que,[0,x])

time=[10**20 for i in range(n+1)]
time[x]=0
visited=[False for i in range(n+1)]

while len(que)>0:
  now,place=heapq.heappop(que)
  if visited[place]:
    continue
  visited[place]=True
  for to,t,k in con[place]:
    to_time=ceil(now/k)*k+t
    if to_time < time[to]:
      time[to]=to_time
      heapq.heappush(que,[to_time,to])

if time[y]==10**20:
  print(-1)
else:
  print(time[y])