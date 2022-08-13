def uqriddistance(x1, y1, x2, y2):
  return (x1-x2)*(x1-x2) + (y1-y2)*(y1-y2)

a, b, c, d = map(int, input().split())

isExist = False
for xd in range(-2, 3):
  for yd in range(-2, 3):
    x = xd + a
    y = yd + b
    A = uqriddistance(x, y, a, b)
    B = uqriddistance(x, y, c, d)
    if A == 5 and B == 5:
      isExist = True
      break

if isExist:
  print("Yes")
else:
  print("No")