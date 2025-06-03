from collections import defaultdict

n,q=map(int, input().split())
dic=defaultdict(int)
ls=[]
for i in range(n):
    dic[i+1] = i
    ls.append(i+1)

for _ in range(q):
  x=int(input())
  original_i=dic[x]
  exchange_i=dic[x]+1
  if exchange_i >= n:
    exchange_i = dic[x]-1
  to_val = ls[exchange_i]
  dic[x] = exchange_i
  dic[to_val] = original_i
  ls[original_i], ls[exchange_i] = to_val, x

print(' '.join(map(str, ls)))
