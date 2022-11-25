"""
1に辿りつく方法は0->1の1通り。
2に辿りつく方法は1->2と0->2の2通り。
3に辿りつく方法は1->3に行く方法と2->3に行く方法。
つまり、1に辿りつく方法+2に辿りつく方法となる。
あとはこれを繰り返していくだけだが、階段に穴が空いているときはそこを通れないので0となる。
"""
n,m = map(int,input().split())
a={}
for i in range(m):
  tmp = int(input())
  a[tmp] = tmp

dp = [0 for i in range(n+1)]
if 1 in a:
  dp[1] = 0
else:
  dp[1] = 1

if n == 1:
  print(dp[1])
  exit()

if 2 in a:
  dp[2] = 0
else:
  if dp[1] == 0:
    dp[2] = 1
  else:
    dp[2] = 2

for i in range(3,n+1):
  if i in a:
    dp[i] = 0
  else:
    fr1 = 0
    if dp[i-1] != 0:
      fr1 = dp[i-1]

    fr2 = 0
    if dp[i-2] != 0:
      fr2 = dp[i-2]

    dp[i] = fr1 + fr2

ans = dp[n]
if ans != 0:
  ans = dp[n]
  ans %= 1000000007
print(ans)