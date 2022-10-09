# 重要例題 bit全探索を2重ループで行う

h,w,k = map(int, input().split())

c = []
for i in range(h):
  chars = list(input())
  c.append(chars)

# 選び方は縦と横のそれぞれを選ぶか選ばないかだからそれぞれ2^h, 2^w通り
ph = 2 ** h
pw = 2 ** w

ans = 0
for phbit in range(ph):
  for pwbit in range(pw):
    black = 0
    for row in range(h):
      for col in range(w):
        if phbit >> row & 1 == 0 and pwbit >> col & 1 == 0:
          if c[row][col] == "#":
            black += 1
    if black == k:
      ans += 1

print(ans)
