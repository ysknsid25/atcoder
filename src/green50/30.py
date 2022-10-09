x = int(input())

for a in range(-10**3, 10**3):
  for b in range(-10**3, 10**3):
    y = a ** 5 - b ** 5
    if x == y:
      print(a, b)
      exit()