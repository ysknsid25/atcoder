from collections import deque
n=int(input())
que=deque()
num=n
if n==1:
  print("A")
  exit()
  
for i in range(120):
  mod=num%2
  num=num//2
  que.appendleft([num,mod])
  if num==1:
    break

ans=[]
ans.append("A")
for num,mod in que:
  ans.append("B")
  if mod ==1:
    ans.append("A")
print("".join(ans))