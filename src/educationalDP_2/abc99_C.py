import sys

def rec(n, memo):
  if n == 0:
    return 0
  if memo[n] != -1:
    return memo[n]

  #! nを全て1円を使って払うときの枚数
  res = n

  #! nを6円を使って払うときの枚数
  pow6 = 6
  x = 1
  while pow6 <= n:
    res = min(res, rec(n-pow6,memo)+1)
    x+=1
    pow6 = 6**x

  #! nを9円を使って払うときの枚数
  pow9 = 9
  x = 1
  while pow9 <= n:
    res = min(res, rec(n-pow9,memo)+1)
    x+=1
    pow9 = 9**x

  memo[n] = res

  return res

n = int(input())
#! Pythonはデフォルトで再帰回数が1000に決まっているので変更しないと通らない
sys.setrecursionlimit(110000)
_MAX_CNT = 110000
memo = [-1 for i in range(_MAX_CNT+1)]
ans = rec(n,memo)
print(ans)