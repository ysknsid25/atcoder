from collections import deque

def bfs(start, r, n):
  visited = [False for i in range(n)]
  cnt = 0
  que = deque()
  que.append(start)
  while 0 < len(que):
    now = que.popleft()
    if visited[now]:
      continue
    cnt += 1
    visited[now] = True
    nxts = r[now]
    for nxt in nxts:
      if visited[nxt]:
        continue
      que.append(nxt)
  return cnt

n,m = map(int, input().split())
r = [[] for i in range(n)]
for i in range(m):
  a,b = map(int, input().split())
  a-=1
  b-=1
  tmp = r[a]
  tmp.append(b)
  r[a] = tmp

ans = 0
for start in range(n):
  ans += bfs(start, r, n)
print(ans)