h,w,x,y = map(int,input().split())

r=[[] for i in range(h+1)]
for i in range(h):
  r[i+1] = [""] + list(input())

s = r[x][y]

if s=="#":
  print(0)
else:
  ans=1
  row = r[x]
  #右
  for i in range(y+1, w+1):
    s=row[i]
    if s==".":
      ans+=1
    else:
      break

  #左
  for i in range(y-1, 0, -1):
    s=row[i]
    if s==".":
      ans+=1
    else:
      break

  #上
  for i in range(x-1, 0, -1):
    s=r[i][y]
    if s==".":
      ans+=1
    else:
      break

  #下
  for i in range(x+1, h+1):
    s=r[i][y]
    if s==".":
      ans+=1
    else:
      break

  print(ans)