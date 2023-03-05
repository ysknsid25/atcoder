def sum_formula(a,b):
    """
    和の公式を使って、a~bまでの和を計算する。
    """
    return (b-a+1)*(a+b)//2

_MOD=998244353
n=int(input())
ans=0
for x in range(1,19):
  if 10**x<=n:
    ans+=sum_formula(1,9*10**(x-1))
    ans%=_MOD
  else:
    ans+=sum_formula(1,n-10**(x-1)+1)
    ans%=_MOD
    break
print(ans)