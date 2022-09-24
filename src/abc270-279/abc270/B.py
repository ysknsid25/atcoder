x, y, z = map(int, input().split())

if x > 0:
  if 0 < y and y < x:
    if y < z:
      print(-1)
    else:
      if z > 0:
        print(x)
      else:
        print(abs(z) * 2 + x)
  else:
    print(abs(x))
else:
  if 0 > y and y > x:
    if y > z:
      print(-1)
    else:
      if z > 0:
        print(abs(z) * 2 + abs(x))
      else:
        print(abs(x))
  else:
    print(abs(x))