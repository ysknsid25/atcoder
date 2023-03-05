x=int(input())
for a in range(-1001,1001):
  for b in range(-1001,1001):
    res = a**5 - b**5
    if res == x:
      print(a,b)
      exit()