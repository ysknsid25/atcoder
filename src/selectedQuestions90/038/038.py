import math
# 最小公倍数
a,b = map(int, input().split())
ans = a * b // math.gcd(a, b)
large = 10 ** 18
if ans > large:
  print("Large")
else:
  print(ans)