from collections import deque

n=int(input())
a=list(map(int,input().split()))

que=deque()
is_n_odd=n%2==1
for i in range(n):
  if is_n_odd:
    if (i+1)%2==0:
      que.append(a[i])
    else:
      que.appendleft(a[i])
  else:
    if (i+1)%2==0:
      que.appendleft(a[i])
    else:
      que.append(a[i])

print(" ".join(map(str,que)))