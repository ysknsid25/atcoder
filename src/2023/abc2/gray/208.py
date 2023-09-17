from collections import defaultdict
n,k=map(int,input().split())
a=list(map(int,input().split()))
d=defaultdict(int)
b=a.copy()
b.sort()
for i in range(n):
    d[b[i]]=i

minimam=0
mod=k
if k>=n:
    minimam=k//n
    mod=k%n
for ai in a:
    if d[ai]+1<=mod:
        print(minimam+1)
    else:
        print(minimam)