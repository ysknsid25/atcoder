from collections import defaultdict
n=int(input())
smap=defaultdict(int)
for i in range(n):
    s=input()
    if smap[s]>0:
        print(s+"("+str(smap[s])+")")
    else:
        print(s)
    smap[s]+=1