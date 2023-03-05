# 近似値による誤差を回避するために全て整数で処理する
import math
a, b, c = map(int, input().split())

x = a
y = pow(c, b)

if x < y:
  print("Yes")
else:
  print("No")