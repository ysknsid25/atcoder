import itertools

n, m = map(int, input().split())
a = list(map(int, input().split()))

c = itertools.combinations(a, m)

maxnum = 0 
for comb in c:
  tmp = 0
  cnt = 1
  for num in comb:
    tmp += cnt * num
    cnt += 1
  maxnum = max(maxnum, tmp)

print(maxnum)