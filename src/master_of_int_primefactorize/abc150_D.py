import math


def lcm(a, b):
    return (a*b)//math.gcd(a, b)


n, m = map(int, input().split())
a = list(map(int, input().split()))

#! 2に関する指数について、指数が全て同じで無ければ半公倍数は存在しない
e = 0
before = e
l = 1
memo = {}
for i in range(n):
    num = a[i]
    e = 0
    #! 一度調べた数は飛ばす
    if num in memo:
        e = memo[num]
    else:
        while num % 2 == 0:
            num /= 2
            e += 1
        odd = a[i]//2
        l = lcm(l, odd)
    if i != 0 and before != e:
        print(0)
        exit()
    before = e
if e == 0 or before != e:
    print(0)
    exit()

#! lがMまでに何回割り切れるかであり、そのうち奇数のモノが答えになる
#! mまで全部計算すると10**9でまわりきらない
ans = 0
to = m//l
for i in range(1, to+1, 2):
    target = i*l
    if target <= m:
        ans += 1
print(ans)
