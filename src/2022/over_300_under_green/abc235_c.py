n,q=map(int,input().split())
a=list(map(int,input().split()))
amap = {}
for i in range(n):
  num=a[i]
  tmp=[]
  if num in amap:
    tmp=amap[num]
  tmp.append(i+1)
  amap[num] = tmp

for i in range(q):
  x,k=map(int,input().split())
  if x in amap:
    idx=k-1
    if k > len(amap[x]):
      print(-1)
    else:
      print(amap[x][idx])
  else:
    print(-1)