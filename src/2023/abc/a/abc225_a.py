import itertools
s=list(input())
h = itertools.permutations(s, len(s))
ans=set(list(h))
print(len(ans))