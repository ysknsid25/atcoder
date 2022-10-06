from collections import deque

s = input()
q = int(input())

ans = deque()
for i in range(len(s)):
  ans.append(s[i])

isReverse = False

for i in range(q):
  tmp = input()
  if len(tmp) == 1:
    isReverse = not isReverse
  else:
    inps = list(map(str, tmp.split()))
    fb = inps[1]
    chr = inps[2]
    if isReverse:
      if fb == "1":
        ans.append(chr)
      else:
        ans.appendleft(chr)
    else:
      if fb == "1":
        ans.appendleft(chr)
      else:
        ans.append(chr)

if isReverse:
  ans.reverse()

res = "".join(ans)
print(res)