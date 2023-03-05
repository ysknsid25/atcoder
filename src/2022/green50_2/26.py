from collections import deque
s = deque()
tmps = input()
q = int(input())

for i in range(len(tmps)):
  s.append(tmps[i])

isReverse = False
for i in range(q):
  query = list(map(str, input().split()))
  if query[0] == "1":
    isReverse = not isReverse
  else:
    if query[1] == "1":
      if isReverse:
        s.append(query[2])
      else:
        s.appendleft(query[2])
    else:
      if isReverse:
        s.appendleft(query[2])
      else:
        s.append(query[2])

ans = "".join(s)
if isReverse:
  # 文字列を反転させる
  ans = ans[::-1]

print(ans)