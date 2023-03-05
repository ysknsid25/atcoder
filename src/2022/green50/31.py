n, k = map(int, input().split())
r,s,p = map(int, input().split())
tarr = list(input())

ans = 0
takahashi = []
for i in range(n):
  t = tarr[i]
  dasitte = 'x'
  if k > i:
    if t == 'r':
      dasitte = 'p'
      ans += p
    elif t == 's':
      dasitte = 'r'
      ans += r
    else:
      dasitte = 's'
      ans += s
  else:
    tt = takahashi[i-k]
    if t == 'r':
      if not tt == 'p':
        dasitte = 'p'
        ans += p
    elif t == 's':
      if not tt == 'r':
        dasitte = 'r'
        ans += r
    else:
      if not tt == 's':
        dasitte = 's'
        ans += s
  takahashi.append(dasitte)
print(ans)