# 重要例題 BFS
from collections import deque

h,w=map(int,input().split())
maze = []
for i in range(h):
  s=list(input())
  maze.append(s)

ans = 0
for i in range(h):
  for j in range(w):
    if maze[i][j] == "#":
      continue
    cnt = [[-1 for i in range(w)] for j in range(h)]
    visited = [[False for i in range(w)] for j in range(h)]
    #! 移動先の数-1が移動数なので、-1で初期化
    #cnt[i][j] = 0
    que = deque()
    que.append((i,j))
    while len(que) > 0:
      ni,nj = que.popleft()
      if not visited[ni][nj]:
        visited[ni][nj] = True
        if 0<=ni-1:
          if maze[ni-1][nj] == ".":
            cnt[ni-1][nj] = cnt[ni][nj] + 1
            que.append((ni-1,nj))
        if ni+1<h:
          if maze[ni+1][nj] == ".":
            cnt[ni+1][nj] = cnt[ni][nj] + 1
            que.append((ni+1,nj))
        if 0<=nj-1:
          if maze[ni][nj-1] == ".":
            cnt[ni][nj-1] = cnt[ni][nj] + 1
            que.append((ni,nj-1))
        if nj+1<w:
          if maze[ni][nj+1] == ".":
            cnt[ni][nj+1] = cnt[ni][nj] + 1
            que.append((ni,nj+1))
    for k in range(h):
      for l in range(w):
        ans = max(ans, cnt[k][l])
print(ans)
