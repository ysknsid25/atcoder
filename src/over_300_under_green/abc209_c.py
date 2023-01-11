n = int(input())
c = list(map(int, input().split()))
sorted_c = c.sort()

_DIV = 10**9+7
ans = 1
for i in range(n):
    ans *= (c[i]-i)
    ans %= _DIV
    if ans == 0:
        print(0)
        exit()
print(ans)
