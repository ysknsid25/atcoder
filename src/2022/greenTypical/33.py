
#! タプルをキーにすることができ、さらに初期値の設定ができる
from collections import defaultdict

n=int(input())
points=[]
p=defaultdict(int)
for i in range(n):
  x,y=map(int,input().split())
  points.append([x,y])
  p[(x,y)]=1

ans=0
for p1 in range(0,n-1):
  for p2 in range(p1+1,n):
    p1_x,p1_y=points[p1]
    p2_x,p2_y=points[p2]
    if p1_x==p2_x or p1_y==p2_y:
      continue
    if p[(p1_x, p2_y)]==1 and p[(p2_x, p1_y)]==1:
      ans+=1

ans//=2
print(ans)
