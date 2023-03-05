import math

a, b, h, m = map(int, input().split())

# 角度の導出は時間算を用いる
# https://study-line.com/tokeizan-matme/
mr = 6 * m
hr = (h / 12 * 360) + 0.5 * m
kakudo = abs(hr - mr)
cos = math.cos(math.radians(kakudo))

# 余弦定理を活用する
c = a ** 2 + b ** 2 - (2 * a * b * cos)

ans = math.sqrt(c)
print(ans)
