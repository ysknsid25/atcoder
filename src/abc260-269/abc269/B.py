slist = []
for i in range(10):
  tmp = input().split()
  s = tmp[0]
  slist.append(list(s))

a = 0
b = 0
c = 0
d = 0
for i in range(10):
  s = slist[i]
  before = "."
  isAllDot = True
  for j in range(10):
    char = s[j]
    if c == 0 and char == "#" and a == 0:
      a = i + 1
      c = j + 1
    if d == 0 and before == "#" and char == ".":
      d = j
      before = char
    if char == "#":
      before = char
      isAllDot = False
  if a > 0 and isAllDot and b == 0:
    b = i

if b == 0:
  b = 10
if d == 0:
  d = 10

print(str(a) + " " + str(b))
print(str(c) + " " + str(d))
