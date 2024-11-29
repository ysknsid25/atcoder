from collections import defaultdict

n=int(input())
a=list(map(int, input().split()))
q=int(input())

d=defaultdict(int)

sum_a=0
for num in a:
  d[num]+=1
  sum_a+=num

for i in range(q):
  b, c = map(int, input().split())
  sum_a+=(c-b)*d[b]
  d[c]+=d[b]
  d[b]=0
  print(sum_a)