def getArray(time):
  ret = []
  if time > 9:
    strh = str(time)
    ret = list(strh)
    ret[0] = int(ret[0])
    ret[1] = int(ret[1])
  else:
    ret.append(0)
    ret.append(time)
  return ret

h,m = map(int, input().split())

ansh = 0
ansm = 0
hi = h
mj = m
for i in range(hi, 24):
  nxth = i
  isFound = False
  for j in range(mj, 60):
    nxtm = j
    har = getArray(nxth)
    mar = getArray(nxtm)
    tmph = har[1]
    tmpm = mar[0]
    har[1] = tmpm
    mar[0] = tmph
    hour = 10*har[0] + har[1]
    minute = 10*mar[0] + mar[1]
    if 0<=hour and hour<=23:
      if 0<=minute and minute<=59:
        isFound = True
        ansh = nxth
        ansm = nxtm
        break
    if nxtm==59:
      mj = 0
  if isFound:
    break
  if nxth == 23:
    hi = 0

print(ansh, ansm)
