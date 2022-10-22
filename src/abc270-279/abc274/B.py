h, w = map(int, input().split())
r = [list(input()) for _ in range(h)]
ans = ["0" for i in range(w)]

for i in range(h):
  for j in range(w):
    char = r[i][j]
    if char == '#':
      num = int(ans[j])
      num += 1
      ans[j] = str(num)

print(" ".join(ans))