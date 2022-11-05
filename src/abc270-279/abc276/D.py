def devide(num, memotwo, memothree):
  if num == 1:
    return 1
  if num in memotwo:
    return memotwo[num]
  if num in memothree:
    return memothree[num]

  if num%2 == 0:
    memotwo[num] = num/2
    return memotwo[num]
  if num%3 == 0:
    memothree[num] = num/3
    return memothree[num]

  return -1

def isAll(a, n):
  bk = -1
  isSame = True
  a.sort(reverse=True)
  bk = a[0]
  for i in range(1,n):
    if bk != a[i]:
      isSame = False
      break
    bk = a[i]
  return isSame

n = int(input())
a = list(map(int, input().split()))
memotwo = {}
memothree = {}
total = 0

isSame = isAll(a, n)
if isSame:
  print(0)
  exit()

while True:
  a.sort(reverse=True)
  num = a[0]
  isSame = isAll(a,n)
  if isSame:
    print(total)
    exit()
  retnum = devide(num, memotwo, memothree)
  if retnum == -1:
    print(-1)
    exit()
  a[0] = retnum
  bk = retnum
  total += 1
