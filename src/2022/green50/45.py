def nCr_mod(n, r, mod):
    nu = 1
    for i in range(n-r+1, n+1):
        nu *= i
        nu %= mod
    de = 1
    for i in range(1, r+1):
        de *= i
        de %= mod
    de_inv = pow(de, -1, mod)
    return nu*de_inv % mod


n, a, b = map(int, input().split())
mod = 10**9+7

ans = pow(2, n, mod)
ans -= 1
ans -= nCr_mod(n, a, mod)
ans -= nCr_mod(n, b, mod)
ans %= mod
print(ans)
