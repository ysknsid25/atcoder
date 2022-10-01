n = int(input())
s = input()
q = int(input())

isReverse = False
strs = "0" + s
slist = list(strs)
for i in range(q):
  t, a, b = map(int, input().split())
  if t == 2:
    isReverse = not isReverse
  else:
    if isReverse:
      if a <= n:
        a += n
      else:
        a -= n
      if b <= n:
        b += n
      else:
        b -= n
    slist[a], slist[b] = slist[b], slist[a]

left = slist[1: n+1]
right = slist[n+1:]

ans = left + right
if isReverse:
  ans = right + left

ans = "".join(ans)
print(ans)