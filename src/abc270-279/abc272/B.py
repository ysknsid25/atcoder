n, m = map(int, input().split())

encount = [[0 for i in range(n)] for i in range(n)]

for i in range(m):
  x = list(map(int, input().split()))
  for j in range(1, len(x)):
    for k in range(1, len(x)):
      me = x[j] - 1
      who = x[k] - 1
      encount[me][who] = 1

isAllEncount = True
for i in range(n):
  myself = i
  isEncount = True
  for j in range(n):
    if myself == j:
      continue
    else:
      if encount[myself][j] == 0:
        isEncount = False
        break

  if not isEncount:
    isAllEncount = False
    break

if isAllEncount:
  print("Yes")
else:
  print("No")