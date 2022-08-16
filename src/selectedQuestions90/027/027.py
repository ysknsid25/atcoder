n = int(input())

rmap = {}
for i in range(0, n):
  s = input()
  day = i + 1
  if s not in rmap:
    rmap[s] = s
    print(day)