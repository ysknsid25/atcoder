n, q = map(int, input().split())

l = []
for i in range(n):
  tmp = list(map(int, input().split()))
  l.append(tmp)

qy = []
for i in range(q):
  tmp = list(map(int, input().split()))
  qy.append(tmp)

for s, t in qy:
  print(l[s-1][t])