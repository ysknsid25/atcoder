import math
n = int(input())

ans = []
i = 1
while i ** 2 <= n:
  if n % i == 0:
    ans.append(i)
    op = n // i
    if op != i:
      ans.append(op)
  i += 1

ans.sort()
for a in ans:
  print(a)