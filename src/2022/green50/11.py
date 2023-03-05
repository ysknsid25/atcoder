n, k = map(int, input().split())

friends = {}
keys = []
for i in range(n):
  a, b = map(int, input().split())
  if a in friends:
    friends[a] += b
  else:
    friends[a] = b
    keys.append(a)

keys.sort()
vi = k
for i in range(0, len(keys)):
  villedge = keys[i]
  if villedge > vi:
    break
  vi += friends[villedge]

print(vi)