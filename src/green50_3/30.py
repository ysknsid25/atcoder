x=int(input())

for a in range(-10**3, 10**3+1):
  for b in range(-10**3, 10**3+1):
    if a**5-b**5==x:
      print(a,b)
      exit()