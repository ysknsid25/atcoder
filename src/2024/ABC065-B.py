from collections import defaultdict

n = int(input())
x = [int(input()) for _ in range(n)]
x.insert(0, 0)
mark = defaultdict(int)

ans = 1
now = 1
while mark[now] != 1:
  mark[now] = 1
  now = x[now]
  ans += 1
  if now == 2:
    print(ans)
    exit()
print(-1)