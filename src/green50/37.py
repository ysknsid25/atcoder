# 重要例題 BFS
from collections import deque


n, m = map(int, input().split())
connect = [[] for i in range(n+1)]

for i in range(m):
    a, b = map(int, input().split())
    connect[a].append(b)
    connect[b].append(a)

visited = [False] * (n+1)
visited[1] = True
que = deque()
que.append(1)
ans = [0 for i in range(n+1)]
while len(que) > 0:
    now = que.popleft()
    for to in connect[now]:
        if not visited[to]:
            ans[to] = now
            visited[to] = True
            que.append(to)

print("Yes")
for i in range(2, n+1):
    print(ans[i])
