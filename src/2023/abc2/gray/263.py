import itertools

n,m=map(int,input().split())
a=[]
for i in range(m):
    a.append(i+1)

for v in itertools.combinations(a, n):
    l=list(v)
    print(' '.join(map(str, l)))