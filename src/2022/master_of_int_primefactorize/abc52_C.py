"""
約数の数は素因数分解から求めることが可能
https://qiita.com/drken/items/a14e9af0ca2d857dad23#5-1-%E7%B4%84%E6%95%B0%E3%81%AE%E5%80%8B%E6%95%B0-%E5%95%8F%E9%A1%8C-5
"""


def pf(n):
    num = int(pow(n, 0.5))
    rem = n
    p = []
    for i in range(2, num+1):
        while(rem % i == 0):
            rem = rem // i
            p.append(i)
    else:
        if rem != 1:
            p.append(rem)
    return p


n = int(input())
res = [1 for i in range(n+1)]
res[0] = 0
i = 1
while i <= n:
    nums = pf(i)
    for num in nums:
        res[num] += 1
    i += 1

ans = 1
for i in range(1, n+1):
    ans *= res[i]
ans %= (10**9+7)
print(ans)
