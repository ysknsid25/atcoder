h,w = map(int, input().split())
osero = [list(input()) for _ in range(h)]

# 行が全て.の場合は削除
osero = [x for x in osero if x.count('.') != w]

h = len(osero)

indexes = []
# 列が全て.の場合は削除
for i in range(0, w):
  tmp = 0
  for j in range(0,h):
    if osero[i][j] == '.':
      tmp += 1
  if tmp != w:
    indexes.append(i)

print(indexes)
for row in osero:
  ans = ''
  for index in indexes:
    ans += row[index]
  print(ans)
