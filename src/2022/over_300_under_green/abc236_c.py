from collections import defaultdict
n,m=map(int,input().split())
s=list(map(str,input().split()))
t=list(map(str,input().split()))
tmap=defaultdict(int)

for st in t:
  tmap[st]=1

for st in s:
  if tmap[st]==1:
    print("Yes")
  else:
    print("No")