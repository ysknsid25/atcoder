from collections import deque
n=int(input())
s=list(input())
que=deque()
que.append(n)
for i in range(n-1,-1,-1):
  c=s[i]
  if c=="L":
    que.append(i)
  else:
    que.appendleft(i)
print(*que)