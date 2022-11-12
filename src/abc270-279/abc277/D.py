n,m = map(int, input().split())
a = list(map(int, input().split()))
suma = 0
t = {}
for i in range(n):
  x = a[i]
  suma += x
  if x in t:
    tmp = t[x]
    tmp[i] = i
    t[x] = tmp    
  else:
    tmp = {}
    tmp[i] = i
    t[x] = tmp

ans = 10**9+1
for i in range(n):
  founded = {}
  search = a
  isContinue = True
  target = i
  sumnum = suma
  while isContinue:
    isContinue = False
    x = search[target]
    if x in t:
      candidates = t[x]
      for c in candidates:
        if c in founded:
          continue
        else:
          founded[target] = True
          sumnum -= x
          isContinue = True
          target = c
    else:
      x = (x+1)%m
      if x in t:
        candidates = t[x]
        for c in candidates:
          if c in founded:
            continue
          else:
            founded[target] = True
            sumnum -= x
            isContinue = True
            target = c
  ans = min(ans, sumnum)
print(ans)