from collections import defaultdict

n, k = map(int, input().split())
c = list(map(int, input().split()))

colors = defaultdict(int)
cnt = 0

for i in range(k):
    colors[c[i]] += 1
    if colors[c[i]] == 1:
        cnt += 1

ans = cnt
for i in range(1, n-k+1):
    colors[c[i-1]] -= 1
    if colors[c[i-1]] == 0:
        cnt -= 1
    colors[c[i+k-1]] += 1
    if colors[c[i+k-1]] == 1:
        cnt += 1
    ans = max(ans, cnt)

print(ans)
