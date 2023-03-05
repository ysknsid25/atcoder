a,b,w = map(int,input().split())

ansmin = 10 ** 15
ansmax = -10 ** 15
g = 1000 * w
for i in range(1, 10**6 + 10):
  if a * i <= g <= b * i:
    ansmin = min(ansmin, i)
    ansmax = max(ansmax, i)

if ansmin == 10 ** 15:
  print("UNSATISFIABLE")
else:
  print(ansmin,ansmax)