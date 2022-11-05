import itertools
n = int(input())
p = list(map(int, input().split()))
l = [i for i in range(1, n+1)]
pl = list(itertools.permutations(l, n))
print(pl)
