n = int(input())

cando = set()
a = 2
while a ** 2 <= n:
  b = 2
  while True:
    if a ** b <= n:
      cando.add(a ** b)
      b += 1
    else:
      break
  a += 1

ans = n - len(cando)
print(ans)