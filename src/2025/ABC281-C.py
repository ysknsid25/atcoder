import heapq

n,m=map(int, input().split())
a=list(map(int, input().split()))
minus_a=[-x for x in a]

heapq.heapify(minus_a)

for _ in range(m):
  num=heapq.heappop(minus_a)
  heapq.heappush(a, num//2)

print(sum(a)*-1)