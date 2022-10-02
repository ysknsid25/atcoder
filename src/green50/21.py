a, b, w = map(int, input().split())

minx = 10 ** 15
maxx = -10 ** 15

"""
条件を満たしているかの判定は、
AX <= 1000W <= BXとなる
(みかん一個あたりの重さはわからんので、一個あたりの最小の重さと最大の重さの総和の範囲にあれば正しい)
このときXが最大となるのは、
W = 1000より、
1000 * 1000 <= BX
つまり、B=1のとき、X = 1000000となる。
これがXの探索範囲である。
"""
r = 10 ** 6 + 1

for x in range(1, r):
  if a * x <= 1000 * w and 1000 * w <= b * x:
    minx = min(minx, x)
    maxx = max(maxx, x)

if minx == 10 ** 15:
  print("UNSATISFIABLE")
else:
  print(minx, maxx)
