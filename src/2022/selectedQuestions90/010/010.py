n = int(input())

aclass = [0] * (n+1)
bclass = [0] * (n+1)

for i in range(0, n):
  c, p = map(int, input().split())
  no = i + 1
  if c == 1:
    aclass[no] = aclass[i] + p
    bclass[no] = bclass[i]
  else:
    bclass[no] = bclass[i] + p
    aclass[no] = aclass[i]

q = int(input())

for i in range(0, q):
  begin, end = map(int, input().split())
  a = aclass[end] - aclass[(begin-1)]
  b = bclass[end] - bclass[(begin-1)]
  print(str(a) + " " + str(b))
