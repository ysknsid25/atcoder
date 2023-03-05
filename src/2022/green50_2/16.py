import itertools

n, k = map(int, input().split())
routes = [i for i in range(1, n)]
cost = []
for i in range(n):
  t = list(map(int, input().split()))
  cost.append(t)

ans = 0
for p in itertools.permutations(routes, len(routes)):
  now = 0
  time = 0
  for next in p:
    time += cost[now][next]
    now = next
  next = 0
  time += cost[now][next]
  if time == k:
    ans += 1
print(ans)