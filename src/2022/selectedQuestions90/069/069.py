# n = 10 ** 8 以上の整数のa^n mod mはTLEするので繰り返し2乗算を使う
# Pythonではpow(a, b, m)を使えばいい。

n, k = map(int, input().split())

mod = 10 ** 9 + 7

if n == 1:
  print(k%mod)
elif n == 2:
  print((k * (k-1))%mod)
else:
  m = n - 2
  p = k -2
  print(k * (k-1)* pow(p, m, mod) % mod)