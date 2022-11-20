def writeMemo(memo, i, x, initVal):
  if i in memo:
    tmp = memo[i]
    tmp += x
    memo[i] = tmp
  else:
    memo[i] = initVal + x
  return memo

def readMemo(memo, i, initVal):
  num = initVal
  if i in memo:
    num = memo[i]
  return num

n = int(input())
a = [0] + list(map(int,input().split()))
q = int(input())
initVal = -1
memo = {}
for i in range(n+1):
  num = a[i]
  memo[i] = num

for cnt in range(q):
  s = input()
  tmp = list(s)
  t = tmp[0]
  if t=="1":
    t,x = map(int, s.split())
    initVal = x
    memo = {}
  elif t=="2":
    t,i,x = map(int, s.split())
    memo = writeMemo(memo, i, x, initVal)
  else:
    t,i = map(int, s.split())
    num = readMemo(memo, i, initVal)
    print(num)