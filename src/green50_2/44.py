from collections import deque
h,w=map(int,input().split())
s=[]
for i in range(h):
  s.append(list(input()))

def explore(w,h,si,sj):
  xw=[1,0,-1,0]
  yh=[0,1,0,-1]
  maze_count=[[-1]*w for i in range(h)]
  maze_count[si][sj]=0
  que=deque()
  que.append([si,sj])
  while 0<len(que):
    nowi,nowj = que.popleft()
    now_count=maze_count[nowi][nowj]
    for y in yh:
      for x in xw:
        nxti=nowi+y
        nxtj=nowj+x
        if nxti<0 or nxti>h-1 or nxtj<0 or nxtj>w-1:
          continue
        #! 上下左右を調べるとき
        if abs(y)+abs(x)==2:
          continue
        if s[nxti][nxtj]=="#":
          continue
        if maze_count[nxti][nxtj]==-1:
          maze_count[nxti][nxtj]=now_count+1
          que.append([nxti,nxtj])
  maxcnt=0
  for i in range(h):
    for j in range(w):
      maxcnt=max(maxcnt,maze_count[i][j])
  return maxcnt

ans=0
for i in range(h):
  for j in range(w):
    if s[i][j]=="#":
      continue
    ans=max(ans,explore(w,h,i,j))
print(ans)