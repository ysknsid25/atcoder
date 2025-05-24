import math


def lcm(a, b):
  return (a*b)//math.gcd(a, b)

a,b,c,d=map(int, input().split())
can_dev_c=(b//c)-(a//c)
can_dev_d=(b//d)-(a//d)
cd_lcm=lcm(c,d)
can_dev_lcm=(b//cd_lcm)-((a-1)//cd_lcm)
ans=a-b+1-can_dev_c-can_dev_d+can_dev_lcm

print(ans)
