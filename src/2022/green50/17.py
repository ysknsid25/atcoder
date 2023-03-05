import math

n = int(input())
sqrt = math.floor(math.sqrt(n))

# setは重複する値は無視したリストを生成してくれる
albumnum = set()
for i in range(2, sqrt+1):
  for j in range(2, 34):
    index = i ** j
    if index <= n:
      albumnum.add(index)
    else:
      break

ans = n - len(albumnum)

print(ans)