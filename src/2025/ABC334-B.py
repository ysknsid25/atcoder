a, m, L, R = map(int, input().split())
L -= a
R -= a

result = 0
if L < 0 < R:
    result = (-L) // m + R // m + 1
elif L > 0:
    result = R // m - L // m
    if L % m == 0:
        result += 1
else:
    result = (-L) // m - (-R) // m
    if (-R) % m == 0:
        result += 1

print(result)