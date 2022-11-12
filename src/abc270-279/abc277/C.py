n = int(input())
radder = {}

for i in range(n):
  a,b = map(int, input().split())
  if a in radder:
    tmp = radder[a]
    tmp.append(b)
    radder[a] = tmp
  else:
    radder[a] = [b]
  if b in radder:
    tmp = radder[b]
    tmp.append(a)
    radder[b] = tmp
  else:
    radder[b] = [a]

from collections import deque
starts = deque()
starts.append(1)
ans = 1
visited = {}
while 0<len(starts):
  start = starts.popleft()
  if start in visited and visited[start]:
    continue
  else:
    visited[start] = True
    if start in radder:
      nexts = radder[start]
      for nxt in nexts:
        ans = max(ans, nxt)
        starts.append(nxt)
print(ans)

