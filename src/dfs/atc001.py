#! 重要例題 DFS
import sys
sys.setrecursionlimit(10000)

def dfs(h,w,seen,g,i,j):
  tox=[1,0,-1,0]
  toy=[0,1,0,-1]
  seen[i][j]=True
  #! 受け取った現在地から四方向を探索する
  for dir in range(4):
    toi=i+tox[dir]
    toj=j+toy[dir]
    #! 範囲外は無視
    if toi<0 or toi>=h or toj<0 or toj>=w:
      continue
    #! 探索済であれば飛ばす
    if seen[toi][toj]:
      continue
    #! 行き先が塀であれば飛ばす
    if g[toi][toj]=="#":
      continue
    #! 再帰的に探索
    dfs(h,w,seen,g,toi,toj)
  return seen

h,w=map(int,input().split())
route=[[[] for j in range(w)] for i in range(h)]
cell=[]
for i in range(h):
  cell.append(list(input()))

#! スタートとゴールを探す
sh,sw,gh,gw=0,0,0,0
for i in range(h):
  for j in range(w):
    if cell[i][j]=="s":
      sh,sw=i,j
    if cell[i][j]=="g":
      gh,gw=i,j

seen = [[False for i in range(w)] for i in range(h)]
seen = dfs(h,w,seen,cell,sh,sw)
if seen[gh][gw]:
  print("Yes")
else:
  print("No")