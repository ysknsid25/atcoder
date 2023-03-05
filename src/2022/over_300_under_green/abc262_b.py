n,m=map(int,input().split())
node=set()
con=[[] for i in range(n+1)]
for i in range(m):
  u,v=map(int,input().split())
  node.add(u)
  node.add(v)

  tmp=con[u]
  tmp.append(v)
  con[u]=tmp

  tmp=con[v]
  tmp.append(u)
  con[v]=tmp


node=list(node)

ans=0
for s in node:
  nxts = con[s]
  for nxt in nxts:
    if nxt <= s:
      continue
    lsts = con[nxt]
    for lst in lsts:
      if lst <= nxt:
        continue
      gs=con[lst]
      for g in gs:
        if g==s:
          ans+=1
print(ans)