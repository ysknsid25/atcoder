import heapq
que=[]
heapq.heapify(que)

n,k=map(int,input().split())
p=list(map(int,input().split()))

index_map={}
for i in range(k):
  heapq.heappush(que,p[i])
  index_map[p[i]]=i+1
print(que[0])

for i in range(k,n):
  x=heapq.heappop(que)
  heapq.heappush(que,max(p[i],x))
  print(que[0])