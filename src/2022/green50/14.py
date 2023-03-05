n = int(input())

points = []
for i in range(n):
  x, y = map(int, input().split())
  points.append([x,y])

isAline = False
for i in range(n):
  for j in range(i+1, n):
    for k in range(j+1, n):
      x1, y1 = points[i]
      x2, y2 = points[j]
      x3, y3 = points[k]
      isAline = (y3-y1)*(x2-x1) == (y2-y1)*(x3-x1)
      if isAline:
        print("Yes")
        exit()

print("No")