n,k = map(int,input().split())
a = [0] + list(map(int, input().split()))

visited = [-1] * (n+1)
visited[1] = 0

now = 1
cnt = 0
cycle = 0

for i in range(10**6):
  cnt += 1
  now = a[now]
  if cnt == k:
    print(now)
    exit()

  if visited[now] == -1:
    visited[now] = cnt
  else:
    #! サイクルはこうやってとる
    cycle = cnt - visited[now]
    break

k -= cnt
k %= cycle

#! 途中の移動を省略し、余りの数だけ調べる
for i in range(k):
  now = a[now]
print(now)