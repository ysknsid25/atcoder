from collections import defaultdict

d = defaultdict(int)
n = int(input())
a = [int(input()) for _ in range(n)]

ans = 0
for i in a:
    if d[i] == 0:
        d[i] += 1
        ans += 1
    else:
        d[i] -= 1
        ans -= 1
print(ans)