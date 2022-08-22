# 重要例題

n = int(input())

# カッコの現れ方は、1bitに対して()の2通りになる
p = 2 ** n

ans = []
# 全探索しないといけないから、外のループはp
for bit in range(p):
  tmp = 0
  out = ""
  # 中はn(bit)の長さだけ調べていくため
  for i in range(n):
    # これはbitのi bit目が1であるための条件
    if (bit >> i) & 1:
      out += "("
      tmp += 1
    else:
      out += ")"
      tmp -= 1

    if tmp < 0:
      break

  # カッコ列が正しいかどうかの判定は、
  # 1.(と)の数が同じ
  # 2.左からi文字目までの時点で(の数が)以上である
  if tmp == 0:
    ans.append(out)

ans.sort()
for out in ans:
  print(out)
