from collections import deque

# 重要例題 BFS
n, m = map(int, input().split())
g = [[] for i in range(n)]

for i in range(m):
  a, b = map(int, input().split())
  # 配列のindexに合わせる
  a -= 1
  b -= 1

  tmp = g[a]
  tmp.append(b)
  g[a] = tmp

starts = [i for i in range(n)]
for city in starts:
  count = 1
  visited = deque()
  visited.appendleft(city)
    
