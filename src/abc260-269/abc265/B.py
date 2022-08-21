n, m, t = map(int, input().split())
a = list(map(int, input().split()))

bonus = {}
for i in range(0, m):
  x, y = map(int, input().split())
  bonus[x] = y

canGoal = False
roomno = 1
for i in range(0, n):
  t -= a[i]
  if t < 0:
    print("No")
    exit()

  roomno += 1
  if roomno in bonus:
    t += bonus[roomno]

  if roomno == n:
    canGoal = True
    break

if canGoal:
  print("Yes")
else:
  print("No")