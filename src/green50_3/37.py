from collections import deque

n,m=map(int,input().split())
con=[[] for i in range(n+1)]
for i in range(m):
  a,b=map(int,input().split())
  con[a].append(b)
  con[b].append(a)

que=deque()
fr_list=[0 for i in range(n+1)]
que.append(1)
while len(que)>0:
  now=que.popleft()
  for nxt in con[now]:
    if fr_list[nxt]==0:
      fr_list[nxt]=now
      que.append(nxt)

print("Yes")
for i in range(2,n+1):
  print(fr_list[i])
