# 重要例題 BFS
from collections import deque


def bfsroom(start, n, connect):
    ret = {}
    visited = [False] * (n+1)
    wherefrom = [0] * (n+1)
    visited[start] = True
    que = deque()
    que.append(start)
    while len(que) > 0:
        now = que.popleft()
        for to in connect[now]:
            if not visited[to]:
                wherefrom[to] = now
                visited[to] = True
                que.append(to)
    ret["visited"] = visited
    ret["wherefrom"] = wherefrom
    return ret


n, m = map(int, input().split())
connect = [[] for i in range(n+1)]

for i in range(m):
    a, b = map(int, input().split())
    connect[a].append(b)
    connect[b].append(a)

ans = 0
for i in range(2, n+1):
    ans += bfsroom(i, n, connect)
print(ans)
