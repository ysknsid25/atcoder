def cansee(r, c, s):
  char = s[r][c]
  if char == "#":
    return 0
  return 1


h, w, x, y = map(int, input().split())

s = []
for i in range(h):
  r = list(input())
  s.append(r)

r = x-1
c = y-1
see = 0
see = cansee(r, c, s)
# 左
l = c-1
while(l > -1):
  tmp = cansee(r, l, s)
  if tmp == 0:
    break
  see += 1
  l -= 1
# 右
for ri in range(c+1, w):
  tmp = cansee(r, ri, s)
  if tmp == 0:
    break
  see += 1
# 下
d = r-1
while(d > -1):
  tmp = cansee(d, c, s)
  if tmp == 0:
    break
  see += 1
  d -= 1
# 上
for u in range(r+1, h):
  tmp = cansee(u, c, s)
  if tmp == 0:
    break
  see += 1

print(see)