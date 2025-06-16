from collections import defaultdict

n,k=map(int, input().split())
a=list(map(int, input().split()))

memo=defaultdict(int)
kinds=set(a)
ans=0

for num in a:
    memo[num] += 1

sorted_items = sorted(memo.items(), key=lambda x: x[1])
for i in range(len(kinds)-k):
    ans += sorted_items[i][1]
print(ans)

