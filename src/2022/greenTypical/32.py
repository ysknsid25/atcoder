import sys
sys.setrecursionlimit(10000000)

def dfs(ans,con,now,pre):
  ans.append(now)
  for to in con[now]:
    if to!=pre:
      dfs(ans,con,to,now)
      ans.append(now)

n=int(input())
con=[[] for i in range(n+1)]
for i in range(n-1):
  a,b=map(int,input().split())
  con[a].append(b)
  con[b].append(a)

for route in con:
  route.sort()

ans=[]
dfs(ans,con,1,-1)
print(*ans)