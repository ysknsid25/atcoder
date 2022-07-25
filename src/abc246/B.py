import math

a, b = map(int, input().split())
d = math.sqrt((a**2 + b**2))

x = a / d
y = b / d

print(str(x) + " " + str(y))
