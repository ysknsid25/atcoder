from collections import deque
s = list(input())
q = int(input())
que = deque(s)
isReverse = False
for i in range(q):
  tmp = list(map(str, input().split()))
  direct = tmp[0]
  if direct == "1":
    isReverse = not isReverse
  else:
    if tmp[1] == "1":
      if isReverse:
        que.append(tmp[2])
      else:
        que.appendleft(tmp[2])
    else:
      if isReverse:
        que.appendleft(tmp[2])
      else:
        que.append(tmp[2])

if isReverse:
  que.reverse()

print("".join(que))
