# 重要例題 BFS
from collections import deque

def bfscity(start, n, connect):
  visited = [False] * (n+1)
  visited[start] = True
  cnt = 1
  que = deque()
  que.append(start)
  while len(que) > 0:
    nowcity = que.popleft()
    for tocity in connect[nowcity]:
      if not visited[tocity]:
        visited[tocity] = True
        cnt += 1
        que.append(tocity)
  return cnt

n, m = map(int, input().split())
connect = [[] for i in range(n+1)]

for i in range(m):
  a, b = map(int, input().split())
  connect[a].append(b)

ans = 0
for i in range(1, n+1):
  ans += bfscity(i, n, connect)
print(ans)