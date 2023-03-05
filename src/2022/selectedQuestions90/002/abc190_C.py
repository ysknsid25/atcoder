# 重要例題 bit全探索の実装
n, m = map(int, input().split())

dish = []
for i in range(m):
  a, b = map(int, input().split())
  tmp = []
  tmp.append(a)
  tmp.append(b)
  dish.append(tmp)

k = int(input())

people = []
for i in range(k):
  c, d = map(int, input().split())
  tmp = []
  tmp.append(c)
  tmp.append(d)
  people.append(tmp)

maxcnt = 0
for bit in range(2 ** k):
  boal = {}
  # 中はn(bit)の長さだけ調べていくため
  for i in range(k):
    select = people[i]
    target = -1
    # これはbitのi bit目が1であるための条件
    if (bit >> i) & 1:
      target = select[1]
    else:
      target = select[0]

    boal[target] = 1

  cnt = 0
  for target in dish:
    a = target[0]
    b = target[1]

    if a in boal and b in boal:
      cnt += 1

  if cnt > maxcnt:
    maxcnt = cnt

print(maxcnt)