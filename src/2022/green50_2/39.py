import heapq
import math

n,m=map(int,input().split())
a=list(map(int,input().split()))
l=[]
for price in a:
  price*=-1
  l.append(price)
heapq.heapify(l)

for i in range(m):
  price=heapq.heappop(l)
  price=math.ceil(price/2)
  heapq.heappush(l,price)

ans=0
for price in l:
  if price<0:
    price*=-1
  ans+=price
print(ans)