x = int(input())
for a in range(-10**3, 10**3):
  for b in range(-10**3, 10**3):
    ans = a**5 - b**5
    if ans == x:
      print(a,b)
      exit()
