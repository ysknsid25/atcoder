from collections import defaultdict

n=int(input())
a=list(map(int,input().split()))
d=defaultdict(int)
c=defaultdict(int)
total=0

for num in a:
  total-=c[num]
  d[num]+=1
  if d[num]>1:
    c[num]=d[num]*(d[num]-1)//2
  total+=c[num]

for num in a:
  exclude=d[num]-1
  if exclude>1:
    print(total-c[num]+(exclude*(exclude-1)//2))
  else:
    print(total-c[num])