n=int(input())
con=[[] for i in range(n+1)]
t=[0]
learn=[False for i in range(n+1)]

# 技nを習得するために必要な技のグラフを作る
for i in range(n):
    tka=list(map(int,input().split()))
    t.append(tka[0])
    k=tka[1]
    for j in range(2,k+2):
        con[i+1].append(tka[j])

from collections import deque

q=deque()
q.appendleft(n)
while len(q)>0:
    now=q.popleft()
    if not learn[now]:
        learn[now]=True
        for to in con[now]:
            q.appendleft(to)

ans=0
for i in range(1,n+1):
    if learn[i]:
        ans+=t[i]

print(ans)