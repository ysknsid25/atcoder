n = int(input())

x = []
y = []
for i in range(n):
  a, b = map(int, input().split())
  x.append(a)
  y.append(b)

for i in range(n):
  for j in range(n):
    for k in range(n):
      if i == j or j == k or k == i:
        continue
      x1 = x[i]
      x2 = x[j]
      a = x[k]
      y1 = y[i]
      y2 = y[j]
      b = y[k]

      if (b - y1) * (x2 - x1) == (y2-y1) * (a-x1):
        print("Yes")
        exit()

print("No")

