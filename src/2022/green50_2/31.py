n, k = map(int, input().split())
r,s,p = map(int, input().split())
t = list(input())
out = []

ans = 0
for i in range(n):
  te = t[i]

  if te == 'r':
    if i<k:
      ans += p
      out.append('p')
    elif k<=i and out[i-k] != 'p':
      ans += p
      out.append('p')
    else:
      out.append('x')
  elif te == 's':
    if i<k:
      ans += r
      out.append('r')
    elif k<=i and out[i-k] != 'r':
      ans += r
      out.append('r')
    else:
      out.append('x')
  else:
    if i<k:
      ans += s
      out.append('s')
    elif k<=i and out[i-k] != 's':
      ans += s
      out.append('s')
    else:
      out.append('x')


print(ans)