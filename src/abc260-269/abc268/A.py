a,b,c,d,e = map(int, input().split())
l = [a,b,c,d,e]
amap = {}
cnt = 0
for i in range(0, 5):
  tmp = l[i]
  if not tmp in amap:
    cnt += 1
    amap[tmp] = 1
print(cnt)