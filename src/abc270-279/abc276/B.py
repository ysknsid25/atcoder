n,m = map(int, input().split())
c = [[] for i in range(n+1)]
d = [0 for i in range(n+1)]

for i in range(m):
  a,b = map(int, input().split())
  d[a] += 1
  d[b] += 1
  tmp = c[a]
  tmp.append(b)
  c[a] = tmp
  
  tmp = c[b]
  tmp.append(a)
  c[b] = tmp

for i in range(1,n+1):
  tmp = c[i]
  if len(tmp) == 0:
    print(0)
    continue
  tmp = sorted(c[i])
  out = str(d[i])
  out2 = ' '.join([str(n) for n in tmp])
  print(out,out2)