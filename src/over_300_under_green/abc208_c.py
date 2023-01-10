from collections import defaultdict
n,k=map(int,input().split())
a=list(map(int,input().split()))
sort_a=a.copy()
sort_a.sort()
dist_map=defaultdict(int)
base=k//n
mod=k%n
for i in range(n):
  no=sort_a[i]
  if n>k:
    if i+1<=k:
      dist_map[no]=1
    else:
      dist_map[no]=0
  elif n>k:
    dist_map[no]=1
  else:
    if i+1<=mod:
      dist_map[no]=base+1
    else:
      dist_map[no]=base

for no in a:
  print(dist_map[no])