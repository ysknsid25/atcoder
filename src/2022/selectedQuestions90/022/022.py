def ukrid(a, b):
  while(a >= 1 and b >= 1):
    if (a < b): 
      b = b%a
    else:
      a = a%b
  if a >= 1:
    return a
  else:
    return b

a, b, c = map(int, input().split())

modres = ukrid(a, b)
modres = ukrid(modres, c)

result = (a//modres-1) + (b//modres-1) + (c//modres-1)

print(result)
