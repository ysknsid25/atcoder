n,m,x = map(int, input().split())

c = []
a = []
for i in range(n):
  tmp = list(map(int, input().split()))
  c.append(tmp[0])
  a.append(tmp[1:])

# カッコの現れ方は、1bitに対して()の2通りになる
p = 2 ** n

ans = 10**15+1
# 全探索しないといけないから、外のループはp
for bit in range(p):
  cost = 0
  us = [0 for i in range(m)]
  # 中はn(bit)の長さだけ調べていくため
  for i in range(n):
    # これはbitのi bit目が1であるための条件
    if (bit >> i) & 1:
      cost += c[i]
      tmp = a[i]
      for j in range(m):
        usj = tmp[j]
        us[j] += usj

  isArchive = True
  for j in range(m):
    usj = us[j]
    if usj < x:
      isArchive = False
      break
  
  if isArchive:
    ans = min(ans, cost)

if ans==10**15+1:
  print(-1)
else:
  print(ans)

