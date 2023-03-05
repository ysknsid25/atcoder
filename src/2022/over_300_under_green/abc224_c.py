def checkAline(x,x1,x2,y,y1,y2):
  return (y2-y)*(x1-x) == (y1-y)*(x2-x)

n=int(input())
xy=[]
for i in range(n):
  x,y=map(int,input().split())
  xy.append([x,y])

ans=0
for i in range(n):
  x,y=xy[i]
  for j in range(i+1,n):
    x1,y1=xy[j]
    for k in range(j+1, n):
      x2,y2=xy[k]
      isAline= checkAline(x,x1,x2,y,y1,y2)
      if not isAline:
        ans+=1
print(ans)