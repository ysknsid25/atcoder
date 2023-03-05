import math

t = int(input())
l, x, y = map(int, input().split())
r = l / 2
q = int(input())

for i in range(q):
  e = int(input())
  kakudo = 360 * (e / t)
  sin = math.sin(math.radians(kakudo))
  cos = math.cos(math.radians(kakudo))

  z = r - (r * cos)
  ye = -r * sin
  xy = math.sqrt(x ** 2 + (y - ye) ** 2)

  dep = math.atan2(z, xy)
  print(math.degrees(dep))