n = int(input())
p = list(map(int, input().split()))

v = []
for i in range(n - 1):
    if p[i] < p[i + 1]:
        if not v or v[-1][0] == '>':
            v.append(('<', 1))
        else:
            v[-1] = (v[-1][0], v[-1][1] + 1)
    else:
        if not v or v[-1][0] == '<':
            v.append(('>', 1))
        else:
            v[-1] = (v[-1][0], v[-1][1] + 1)

sz = len(v)
ans = 0
for i in range(1, sz - 1):
    if v[i][0] == '>':
        ans += v[i - 1][1] * v[i + 1][1]

print(ans)
