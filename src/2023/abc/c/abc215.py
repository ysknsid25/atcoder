import itertools

s,k=input().split()
s=list(s)
k=int(k)

all = itertools.permutations(s, len(s))
res=[]
for x in all:
    res.append("".join(x))
print(sorted(list(set(res)))[k-1])