import math
n, k, x = map(int, input().split())
a = list(map(int, input().split()))

remainList = a
couponTotal = 0
paysum = 0

for i in range(0, n):
    remainList[i] = a[i] % k
    couponTotal += math.floor(a[i]/x)
    paysum += a[i]

if k <= couponTotal:
    result = paysum - (couponTotal*x)
else:
    result = paysum - (couponTotal*x)
    remaincoupon = couponTotal - k
    remainList.sort(reverse=True)
    for i in range(0, len(remainList)):
        result -= remainList[i]
        remaincoupon -= 1
        if result == 0 or remaincoupon == 0:
            break
print(result)
