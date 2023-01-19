n,m=map(int,input().split())
b=[]
for i in range(n):
  tmp=list(map(int,input().split()))
  b.append(tmp)

isValid=True

# 1行目の値が単調増加かどうか
before=b[0][0]
for i in range(1,m):
  if (before+1)==b[0][i]:
    before=b[0][i]
    continue
  else:
    isValid=False
    break

if not isValid:
  print("No")
  exit()

#! Bの1行目がAの範囲に収まっているかどうか
target = b[0]
l=(b[0][0]-1)//7
r=(b[0][m-1]-1)//7
if l!=r:
  print("No")
  exit()

for i in range(1,n):
  before=b[i-1]
  now=b[i]
  for j in range(m):
    if j<m-1:
      nxt=now[j+1]
      if nxt==(now[j]+1):
        if (before[j]+7) == now[j]:
          continue
        else:
          isValid = False
          break
      else:
        isValid = False
        break
    else:
        if (before[j]+7) == now[j]:
          continue
        else:
          isValid = False
          break

if isValid:
  print("Yes")
else:
  print("No")
