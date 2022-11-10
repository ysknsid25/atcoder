a,b,w = map(int, input().split())
w *= 1000

minans = 10 ** 15
maxans = -10 ** 15
for x in range(1, 10**6+1):
  if a*x <= w <= b*x:
    minans = min(minans, x)
    maxans = max(maxans, x)
if minans == 10**15:
  print("UNSATISFIABLE")
else:
  print(minans, maxans)