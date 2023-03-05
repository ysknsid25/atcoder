n,k = map(int, input().split())
pl = list(map(int, input().split()))
exp = []
sectotal = 0
for p in pl:
  tmpexp = (p+1)/2
  sectotal += tmpexp
  exp.append(sectotal)

maxp = -10 ** 15
for i in range(0, n-k+1):
  to = i+k-1
  if i==0:
    maxp = max(maxp, exp[to])
  else:
    fr = i-1
    secexp = exp[to]-exp[fr]
    maxp = max(maxp, secexp)

print(maxp)