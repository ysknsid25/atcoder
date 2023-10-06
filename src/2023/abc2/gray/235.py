from collections import defaultdict
n,q=map(int,input().split())
a=list(map(int,input().split()))
existMap=defaultdict(list)
for i in range(n):
    existMap[a[i]].append(i+1)

for i in range(q):
    x,k=map(int,input().split())
    if x not in existMap:
        print(-1)
    else:
        numlist=existMap[x]
        if k > len(numlist):
            print(-1)
        else:
            print(numlist[k-1])
