import math
def lcm(a, b):
  return (a*b)//math.gcd(a,b)

a,b = map(int, input().split())

ans = lcm(a,b)
print(ans)