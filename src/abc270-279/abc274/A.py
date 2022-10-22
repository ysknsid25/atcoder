import math
a, b = map(int, input().split())

n = 3  # 切り捨てしたい桁
x = b/a
y = round(x, 3)
print('{:.3f}'.format(y))