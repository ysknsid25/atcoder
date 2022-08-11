import math
n, k, x = map(int, input().split())
a = list(map(int, input().split()))

# 最初の金額の最大値
remainList = a
couponTotal = 0
paysum = 0
discountsum = k*x

for i in range(0, n):
    tmpa = a[i]
    remainList[i] = tmpa % x
    couponTotal += tmpa//x
    paysum += tmpa
ans = paysum
if k <= couponTotal:
    ans = paysum - discountsum
    print(ans)
else:
    ans = paysum - (x*couponTotal)
    rem = k - couponTotal
    remainList.sort(reverse=True)
    ans -= sum(remainList[:rem])
    print(ans)
