import itertools
n, k = map(int, input().split())

cities = [i for i in range(1, n)]

t = []
for i in range(n):
  inputs = list(input().split(' '))
  t.append(inputs)

routecnt = 0
for route in itertools.permutations(cities, n-1):
  cost = 0
  before = 0
  for next in route:
    cost += int(t[before][next])
    before = next
  next = 0
  cost += int(t[before][next])
  if cost == k:
    routecnt += 1

print(routecnt)
