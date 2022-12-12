n=int(input())
con=[[] for i in range(n)]
v=set()
for i in range(n-1):
  fr,to,w=map(int,input().split())
  fr-=1
  to-=1
  con[fr].append([to,w])
  con[to].append([fr,w])
  v.add(fr)
  v.add(to)
seen=[-1 for i in range(len(list(v)))]

def dfs(seen,g,v,c):
    seen[v]=c
    for to,w in g[v]:
        if seen[to]!=-1:
            continue
        if w%2==1:
          c=1-c
        #! 再帰的に探索
        dfs(seen,g,to,c)
    return seen

seen=dfs(seen,con,0,0)
for c in seen:
  print(c)