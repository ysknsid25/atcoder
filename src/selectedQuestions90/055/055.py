import itertools
n, p, q = map(int, input().split())
tmp = list(map(int, input().split()))
cs = itertools.combinations(tmp, 5)
res = 0
for c in cs:
  if (c[0]% p * c[1]% p * c[2]% p * c[3]% p * c[4]% p) == q:
    res += 1
print(res)