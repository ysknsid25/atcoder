from functools import reduce
from math import gcd

N, X = map(int, input().split())
x = list(map(int, input().split()))

diff = [abs(X - xi) for xi in x]

g = reduce(gcd, diff)
print(g)
