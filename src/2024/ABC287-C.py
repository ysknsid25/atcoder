def dfs(visited, g, v):
    visited[v] = True
    for to in g[v]:
        if visited[to]:
          continue
        #! 再帰的に探索
        dfs(visited, g, to)
    return visited

n,m = map(int, input().split())
graph = [[] for _ in range(0,n)]
visited = [False for _ in range(0,n)]

for i in range(m):
  a,b = map(int, input().split())
  a-=1
  b-=1
  graph[a].append(b)
  graph[b].append(a)

dfs(visited, graph, 0)
if not all(visited):
  print('No')
  exit()

edge = 0
for node in graph:
  if len(node) == 1:
    edge += 1
  elif len(node) != 2:
    print('No')
    exit()

if edge == 2:
  print('Yes')
else:
  print('No')