n, k = map(int, input().split())
p = list(map(int, input().split()))
c = []
for i in range(n):
  me = p[i]
  tmp = (1+me)/2
  if i > 0:
    tmp += c[i-1]
  c.append(tmp)

ans = -10 ** 15
for i in range(n-k+1):
  res = c[i+k-1]
  if i > 0:
    res = c[i+k-1] - c[i-1]
  ans = max(ans, res)

print(ans)