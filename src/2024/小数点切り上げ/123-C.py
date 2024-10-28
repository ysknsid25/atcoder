import math

n=int(input())
a=int(input())
b=int(input())
c=int(input())
d=int(input())
e=int(input())

# 一番時間がかかるボトルネックを見つける
bottle_neck = min(a, b, c, d, e)
# 1. 最初にボトルネックの場所まで運ばれて来るまで
# 2. ボトルネックを通る回数
# 3. 最後の人がボトルネックからゴールまで
# 1 + 3 の時間は、5つの間のボトルネックまでのfrom + toなので絶対4
ans = math.ceil(n / bottle_neck) + 4
print(ans)