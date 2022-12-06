"""
問題を簡単なものに変えていく。
https://qiita.com/drken/items/a14e9af0ca2d857dad23#6-4-%E7%B4%84%E6%95%B0%E3%81%AE%E6%A7%8B%E9%80%A0%E3%82%92%E7%9F%A5%E3%82%8B
"""


def gcd(x, y):
    if y == 0:
        return x
    return gcd(y, x % y)


def prime_factorize(N):
    if N == 1:
        return [1]
    prime_list = []
    i = 2
    while i*i <= N:
        if N % i == 0:
            prime_list.append(i)
            N //= i
        else:
            i += 1
    if N != 1:
        prime_list.append(N)
    return prime_list


a, b = map(int, input().split())
c = gcd(a, b)
p = prime_factorize(c)
if len(p) == 1 and p[0] == 1:
    ans = 1
else:
    p = set(p)
    ans = 1 + len(p)
print(ans)
