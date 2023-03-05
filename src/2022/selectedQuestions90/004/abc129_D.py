
h, w = map(int, input().split())

arr = []
for i in range(0, h):
  tmp = list(map(str, input().split()))
  arr.append(list(tmp[0]))

r = [[0] * w] * h
for i in range(0, h):
  rowarr = arr[i]
  tmparr = [0] * w
  for j in range(0, w):
    mytxt = rowarr[j]
    cnt = 0
    if mytxt == "#": 
      continue
    else:
      # 右半分を調べる
      rend = w
      rnow = j
      rcnt = 0
      while(rnow < rend):
        rtxt = rowarr[rnow]
        if rtxt == ".":
          rcnt += 1
        else:
          break
        rnow += 1
      tmparr[j] = rcnt
  r[i] = tmparr

l = [[0] * w] * h
for i in range(0, h):
  rowarr = arr[i]
  tmparr = [0] * w
  for j in range(0, w):
    mytxt = rowarr[j]
    cnt = 0
    if mytxt == "#": 
      continue
    else:
      lend = 0
      lnow = j-1
      lcnt = 0
      while(lnow >= lend):
        ltxt = rowarr[lnow]
        if ltxt == ".":
          lcnt += 1
        else:
          break
        lnow -= 1
      tmparr[j] = lcnt
  l[i] = tmparr

arr_t = [list(x) for x in zip(*arr)]

u = [[0] * h] * w
for i in range(0, w):
  rowarr = arr_t[i]
  tmparr = [0] * h
  for j in range(0, h):
    mytxt = rowarr[j]
    cnt = 0
    if mytxt == "#": 
      continue
    else:
      # 右半分を調べる
      rend = h
      rnow = j
      rcnt = 0
      while(rnow < rend):
        rtxt = rowarr[rnow]
        if rtxt == ".":
          rcnt += 1
        else:
          break
        rnow += 1
      tmparr[j] = rcnt
  u[i] = tmparr

d = [[0] * h] * w
for i in range(0, w):
  rowarr = arr_t[i]
  tmparr = [0] * h
  for j in range(0, h):
    mytxt = rowarr[j]
    cnt = 0
    if mytxt == "#": 
      continue
    else:
      # 左半分を調べる
      lend = 0
      lnow = j-1
      lcnt = 0
      while(lnow >= lend):
        ltxt = rowarr[lnow]
        if ltxt == ".":
          lcnt += 1
        else:
          break
        lnow -= 1
      tmparr[j] = lcnt
  d[i] = tmparr

maxcnt = 0
for i in range(0, h):
  for j in range(0, w):
    tmpmax = l[i][j] + r[i][j] + u[j][i] + d[j][i] -1
    if tmpmax > maxcnt:
      maxcnt = tmpmax

print(maxcnt)
