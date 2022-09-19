n, x = map(int, input().split())
a = list(map(int, input().split()))

newlist = []
for i in range(n):
  tmp = a[i]
  if tmp != x:
    newlist.append(tmp)

print(*newlist)
