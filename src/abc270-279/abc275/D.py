# 重要例題:メモ化再帰
# そのままやるとTLEする。なぜなら、n=100000とかになると、
# k=3とかk=1のパターンが大量に呼び出されるからである。
# が、k=3とかは一回計算したら、マップに放り込んでおけば再計算の必要はない。
# これがメモ化再帰
memo = {}
def f(k, memo):
  if k in memo:
    return memo[k]
  if k == 0:
    return 1
  a = k/2
  b = k/3
  if k%2 != 0:
    a = k//2
  if k%3 != 0:
    b = k//3
  nexta = f(a,memo)
  nextb = f(b,memo)
  next = nexta + nextb
  memo[k] = next
  return next

n = int(input())
print(f(n, memo))