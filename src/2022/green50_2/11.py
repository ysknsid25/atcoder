n, k = map(int, input().split())

f = []
for i in range(n):
  a, b = map(int, input().split())
  f.append([a,b])
f.sort()

now = 0
now += k

for i in range(n):
  fv = f[i][0]
  fm = f[i][1]
  if fv <= now:
    now += fm
  else:
    break 

print(now)