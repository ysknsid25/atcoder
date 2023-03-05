import itertools
n,k = map(int, input().split())
t = []
for i in range(n):
  tmp = list(map(int, input().split()))
  t.append(tmp)

ans = 0
l = [i for i in range(1,n)]
for p in itertools.permutations(l):
  fr = 0
  time = 0
  for to in p:
    time += t[fr][to]
    fr = to
  to = 0
  time += t[fr][to]
  if time==k:
    ans += 1

print(ans)