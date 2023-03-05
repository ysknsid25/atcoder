# 包除原理
# 0,9を含まない数列の数 = 0を含まない数列の数 + 9を含まない数列の数 - 0も9も含まない数列の数
# 0,9を含む数列 = 数列の全体数 - 0,9を含まない数列の数
# 以上の式を変形して、
# 0,9を含む数列 = 数列の全体数 - 0を含まない数列の数 - 9を含まない数列の数 + 0も9も含まない数列の数

n = int(input())
mod = 10**9+7

all = pow(10, n, mod)
exzero = pow(9, n, mod)
exnine = pow(9, n, mod)
exzeronine = pow(8, n, mod)

ans = all - exzero - exnine + exzeronine
ans %= mod
print(ans)