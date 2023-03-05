ans = 0
n, x = map(int, input().split())
intx = x * 10000

total = 0
for i in range(n):
    ans += 1
    v, p = map(int, input().split())
    intv = v * 100
    drink = intv * p
    total += drink
    if total > intx:
        print(ans)
        exit()

print(-1)
