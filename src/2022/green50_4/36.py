n,k=map(int,input().split())
a=[0]+list(map(int,input().split()))
amap = {}
now = a[1]
cnt = 1
cycle = 0
while True:
  now = a[now]
  cnt += 1
  if now in amap:
    cycle = cnt - amap[now]
    break
  else:
    amap[now] = cnt
  if cnt == k:
    print(now)
    exit()

k -= cnt
k %= cycle
for i in range(k):
  now = a[now]
print(now)