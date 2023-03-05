n, m, x = map(int, input().split())

c = []
a = []
for i in range(n):
  tmp = list(map(int, input().split()))
  c.append(tmp[0])
  a.append(tmp[1:])

# 選び方は、i番目の本を選ぶor選ばないなので、2^n通り
p = 2 ** n

ans = 10 ** 15
# 全探索しないといけないから、外のループはp
for bit in range(p):
  money = 0
  ustd = [0 for i in range(m)]
  # 中はn(bit)の長さだけ調べていくため
  for i in range(n):
    if (bit >> i) & 1:
      money += c[i]
      for j in range(m):
        ustd[j] = ustd[j] + a[i][j]

  isOverX = True
  for j in range(m):
    if ustd[j] < x:
      isOverX = False
      break
  
  if isOverX:
    ans = min(ans, money)

if ans == 10 ** 15:
  ans = -1

print(ans)