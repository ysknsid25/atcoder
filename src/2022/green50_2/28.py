h,w,k = map(int, input().split())
c = []
for i in range(h):
  tmp = list(input())
  c.append(tmp)

# 選び方は、i番目の本を選ぶor選ばないなので、2^n通り
ph = 2 ** h
pw = 2 ** w

ans = 0
# 全探索しないといけないから、外のループはp
for bitph in range(ph):
  for bitpw in range(pw):
    black = 0
    # 中はn(bit)の長さだけ調べていくため
    for i in range(h):
      for j in range(w):
        if (bitph >> i) & 1 == 0 and (bitpw >> j) & 1 == 0:
          if c[i][j] == "#":
            black += 1

    if black == k:
      ans += 1

print(ans)