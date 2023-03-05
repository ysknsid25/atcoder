n = int(input())

mmap = {}
for i in range(n):
  s, t = map(str, input().split())
  mmap[s] = int(t)

sortedMap = sorted(mmap.items(), key=lambda x: x[1], reverse=True)
ans = sortedMap[1][0]
print(ans)