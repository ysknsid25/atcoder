n, m, x = map(int, input().split())

c = []
a = []
for i in range(n):
  tmp = list(map(int,input().split()))
  c.append(tmp[0])
  a.append(tmp[1:])

# カッコの現れ方は、1bitに対して()の2通りになる
p = 2 ** n

ans = []
minc = 10 ** 15
# 全探索しないといけないから、外のループはp
for bit in range(p):
  skills = [0 for i in range(m)]
  tmpc = 0
  # 中はn(bit)の長さだけ調べていくため
  for i in range(n):
    # これはbitのi bit目が1であるための条件
    if (bit >> i) & 1:
      tmpc += c[i]
      for j in range(m):
        skills[j] += a[i][j]

  isSuccess = True
  for j in range(m):
    skill = skills[j]
    if skill < x:
      isSuccess = False
      break

  if isSuccess:
    minc = min(minc, tmpc)

if minc == 10 ** 15:
  print(-1)
else:
  print(minc)