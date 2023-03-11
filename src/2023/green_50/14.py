n=int(input())

dots = []
for i in range(n):
    x,y=map(int,input().split())
    dots.append([x,y])

for i in range(n):
  for j in range(n):
      for k in range(n):
        if i==j or i==k or j==k:
          continue
        x,y=dots[i]
        x1,y1=dots[j]
        x2,y2=dots[k]
        l=(x2-x1)*(y-y1)
        r=(y2-y1)*(x-x1)
        if l==r:
          print("Yes")
          exit()

print("No")