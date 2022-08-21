n, m = map(int, input().split())

graph = {}
for i in range(0, m):
  a, b = map(str, input().split())
  if a in graph:
    tmp = graph[a]
    tmp.append(b)
    graph[a] = tmp
  else:
    graph[a] = [b]

  if b in graph:
    tmp = graph[b]
    tmp.append(a)
    graph[b] = tmp
  else:
    graph[b] = [a]

anscnt = 0
for k in graph:
  cnt = 0
  nodes = graph[k]
  for i in nodes:
    if int(i) < int(k):
      cnt += 1
  
  if cnt == 1:
    anscnt += 1

print(anscnt)