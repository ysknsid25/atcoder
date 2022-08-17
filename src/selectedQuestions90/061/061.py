from collections import deque

d = deque()

q = int(input())

for i in range(0, q):
  t, x = map(int, input().split())
  if t == 1:
    d.appendleft(x)
  elif t == 2:
    d.append(x)
  else:
    index = x - 1
    print(d[index])