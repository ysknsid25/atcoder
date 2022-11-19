n = int(input())
a = [0] + list(map(int,input().split()))
q = int(input())
initVal = -1
isInit = False
beforecnt = -1

for cnt in range(q):
  s = input()
  tmp = list(s)
  t = tmp[0]
  if t=="1":
    t,x = map(int, s.split())
    initVal = x
    if isInit:
      beforecnt = cnt
    isInit = True
  elif t=="2":
    t,i,x = map(int, s.split())
    if initVal != a[i]:
      a[i] += x
    else:
      a[i] = initVal + x
  else:
    t,i = map(int, s.split())
    if not isInit and initVal != a[i]:
      print(a[i])
    else:
      print(initVal)