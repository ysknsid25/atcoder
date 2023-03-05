from collections import deque

n, m = map(int, input().split())
con = [[] for i in range(n+1)]
for i in range(m):
  a, b = map(int, input().split())
  con[a].append(b)

def bfs(start, n, con):
  count = 1
  visited = [False for i in range(n+1)]
  visited[start] = True
  visit = deque()
  visit.append(start)
  while 0 < len(visit):
    city = visit.popleft()
    for tocity in con[city]:
      if not visited[tocity]:
        visited[tocity] = True
        count += 1
        visit.append(tocity)
  return count

ans = 0
for i in range(1, n+1):
  ans += bfs(i, n, con)

print(ans)