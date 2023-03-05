n = int(input())
s = list(input())

slen = len(s)
mid = slen//2
isReverse = False

q = int(input())
for i in range(q):
  t,a,b = map(int, input().split())
  a-=1
  b-=1
  if t==2:
    isReverse = not isReverse
  else:
    if isReverse:
      a = (mid+a)%slen
      b = (mid+b)%slen
    s[a], s[b] = s[b], s[a]

if isReverse:
  left = s[0:mid]
  right = s[mid:]
  s = right + left
ans = "".join(s)
print(ans)