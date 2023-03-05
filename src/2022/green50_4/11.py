n,k =map(int, input().split())
fr = {}
for i in range(n):
  a,b = map(int, input().split())
  if a in fr:
    tmp = fr[a]
    tmp += b
    fr[a] = tmp
  else:
    fr[a] = b
fr = sorted(fr.items())

now = k
for a,b in fr:
  if a <= now:
    now += b

print(now)