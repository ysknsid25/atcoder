n = int(input())
l = []
for i in range(n):
  x,y = map(int, input().split())
  l.append([x,y])

for i in range(n):
  for j in range(i+1,n):
    for k in range(j+1, n):
      x,y = l[i]
      x1,y1 = l[j]
      x2,y2 = l[k]
      if (x2-x1)*(y-y1) == (y2-y1)(x-x1):
        print("Yes")
        exit()
print("No")