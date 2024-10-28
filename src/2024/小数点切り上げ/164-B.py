a,b,w = map(int, input().split())
w *= 1000

ans_min = 10**9
ans_max = -10**9
for x in range(1, 1000 * 1000 + 1):
    if a * x <= w and w <= b * x:
        ans_min = min(ans_min, x)
        ans_max = max(ans_max, x)

if ans_min == 10**9:
    print("UNSATISFIABLE")
elif ans_max == -10**9:
    print("UNSATISFIABLE")
else:
    print(ans_min, ans_max)
    