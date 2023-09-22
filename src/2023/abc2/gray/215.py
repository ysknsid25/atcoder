import itertools
s, k = map(str, input().split())
k=int(k)
n=len(s)

l=[]
for v in itertools.permutations(s, n):
    l.append(v)
l=set(l)
l=list(l)
l.sort()
print("".join(l[k-1]))