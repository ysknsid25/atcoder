from collections import defaultdict
import math

def combinations_count(n, k):
    return math.factorial(n) // (math.factorial(n - k) * math.factorial(k))

n=int(input())
a=list(map(int,input().split()))
ap_map=defaultdict(int)
same=0
for num in a:
  same+=ap_map[num]
  ap_map[num]+=1

comb=combinations_count(n, 2)
ans=comb-same
print(ans)