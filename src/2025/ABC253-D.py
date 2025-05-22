import math


def lcm(a, b):
    return (a*b)//math.gcd(a, b)

n,a,b=map(int,input().split())
max_a=n//a
max_b=n//b
ab_lcm=lcm(a,b)
max_lcm=n//ab_lcm

sum_a=a*max_a*(max_a+1)//2
sum_b=b*max_b*(max_b+1)//2
sum_lcm=ab_lcm*max_lcm*(max_lcm+1)//2
n_sum=n*(n+1)//2

print(n_sum-(sum_a+sum_b-sum_lcm))